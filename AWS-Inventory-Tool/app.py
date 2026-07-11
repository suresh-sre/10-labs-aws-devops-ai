"""AWS Inventory Tool entrypoint."""

from __future__ import annotations

import logging
from pathlib import Path

import click

from aws.session import create_aws_session
from config import Config
from inventory.ec2 import collect_ec2_instances
from inventory.rds import collect_rds_instances
from inventory.s3 import collect_s3_buckets
from reports.csv_report import write_csv_report
from reports.html_report import HtmlReportEntry, write_html_report
from utils.logger import configure_logging


@click.command()
@click.option("--ec2", is_flag=True, default=False, help="Collect EC2 inventory.")
@click.option("--s3", is_flag=True, default=False, help="Collect S3 inventory.")
@click.option("--rds", is_flag=True, default=False, help="Collect RDS inventory.")
@click.option("--all", "collect_all", is_flag=True, default=False, help="Collect all supported inventories.")
@click.option("--profile", default=None, help="AWS profile to use from ~/.aws/credentials or ~/.aws/config.")
@click.option("--output-dir", default=None, help="Override output directory from .env.")
@click.option("--dashboard", is_flag=True, default=False, help="Generate HTML dashboard report.")
def main(
    ec2: bool,
    s3: bool,
    rds: bool,
    collect_all: bool,
    profile: str | None,
    output_dir: str | None,
    dashboard: bool,
) -> None:
    configure_logging()
    logger = logging.getLogger(__name__)

    if not any([ec2, s3, rds, collect_all]):
        click.echo("No inventory target selected. Use --ec2, --s3, --rds, or --all.")
        raise click.Abort()

    config = Config.load()
    if profile:
        config.aws_profile = profile
    if output_dir:
        config.output_dir = Path(output_dir)
    output_path = config.ensure_output_dir()
    session = create_aws_session(
        region_name=config.aws_region,
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_key,
        profile_name=config.aws_profile,
    )

    reports = []
    targets = ["ec2", "s3", "rds"] if collect_all else [name for name, enabled in [("ec2", ec2), ("s3", s3), ("rds", rds)] if enabled]

    if "ec2" in targets:
        ec2_client = session.client("ec2")
        instances = collect_ec2_instances(ec2_client)
        ec2_report = write_csv_report(output_path, "ec2_inventory.csv", instances)
        logger.info("EC2 inventory report wrote to %s", ec2_report)
        reports.append(HtmlReportEntry(name="EC2", filename=ec2_report.name, count=len(instances)))

    if "s3" in targets:
        s3_client = session.client("s3")
        buckets = collect_s3_buckets(s3_client)
        s3_report = write_csv_report(output_path, "s3_inventory.csv", buckets)
        logger.info("S3 inventory report wrote to %s", s3_report)
        reports.append(HtmlReportEntry(name="S3", filename=s3_report.name, count=len(buckets)))

    if "rds" in targets:
        rds_client = session.client("rds")
        rds_instances = collect_rds_instances(rds_client)
        rds_report = write_csv_report(output_path, "rds_inventory.csv", rds_instances)
        logger.info("RDS inventory report wrote to %s", rds_report)
        reports.append(HtmlReportEntry(name="RDS", filename=rds_report.name, count=len(rds_instances)))

    if dashboard:
        html_report = write_html_report(output_path, reports)
        logger.info("HTML dashboard generated at %s", html_report)
        click.echo(f"Dashboard created: {html_report}")

    click.echo("Inventory export completed.")


if __name__ == "__main__":
    main()

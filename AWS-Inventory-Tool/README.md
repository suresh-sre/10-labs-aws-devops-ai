# AWS-Inventory-Tool

A Python-based inventory utility that discovers AWS resources, collects metadata, and exports reports in CSV or JSON formats.

## What this project does
- Connects to AWS using `boto3` and environment-based credentials.
- Enumerates common AWS resources such as EC2, S3, RDS, and IAM.
- Generates structured inventory reports for auditing and cost planning.
- Supports a CLI-driven workflow with export targets under `output/`.

## Key features
- AWS resource discovery
- Report generation in CSV/JSON
- Configurable output directory
- Built as a modular tool for easy extension

## Folder structure
- `app.py` — startup entrypoint
- `config.py` — environment configuration and validation
- `inventory/` — resource discovery and inventory collection
- `aws/` — AWS-specific helpers and session management
- `reports/` — report rendering and export logic
- `output/` — generated inventory files
- `utils/` — shared helper utilities
- `tests/` — unit tests and validation
- `docs/` — architecture and API planning

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and update AWS credentials.
3. Run the tool with one or more inventory targets:
   ```bash
   python app.py --all --dashboard
   python app.py --ec2 --s3 --output-dir=output/reports --dashboard
   python app.py --rds
   ```

## CLI Options
- `--ec2` : collect EC2 inventory
- `--s3` : collect S3 bucket inventory
- `--rds` : collect RDS instance inventory
- `--all` : collect EC2, S3, and RDS inventories
- `--profile` : AWS profile to use from `~/.aws/credentials` or `~/.aws/config`
- `--output-dir` : override output directory from `.env`
- `--dashboard` : generate an HTML dashboard report

## Environment variables
- `AWS_REGION` (optional if a default region is set in AWS config)
- `AWS_ACCESS_KEY_ID` (optional if using shared credentials/profile)
- `AWS_SECRET_ACCESS_KEY` (optional if using shared credentials/profile)
- `AWS_PROFILE` (optional; preferred when using named profiles)
- `OUTPUT_DIR`

## Next step
I recommend confirming the README text, then I’ll generate the detailed `requirements.txt` and `.gitignore` for this project.

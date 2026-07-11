from __future__ import annotations

import logging
from typing import Any

import boto3


logger = logging.getLogger(__name__)


def collect_rds_instances(rds_client: boto3.client) -> list[dict[str, Any]]:
    logger.info("Collecting RDS instance inventory...")
    paginator = rds_client.get_paginator("describe_db_instances")
    instances: list[dict[str, Any]] = []

    for page in paginator.paginate():
        for db_instance in page.get("DBInstances", []):
            instances.append(
                {
                    "DBInstanceIdentifier": db_instance.get("DBInstanceIdentifier"),
                    "DBInstanceClass": db_instance.get("DBInstanceClass"),
                    "Engine": db_instance.get("Engine"),
                    "EngineVersion": db_instance.get("EngineVersion"),
                    "Status": db_instance.get("DBInstanceStatus"),
                    "AvailabilityZone": db_instance.get("AvailabilityZone"),
                    "MultiAZ": db_instance.get("MultiAZ"),
                }
            )

    logger.info("Collected %d RDS instances", len(instances))
    return instances

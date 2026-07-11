from __future__ import annotations

import logging
from typing import Any

import boto3


logger = logging.getLogger(__name__)


def collect_ec2_instances(ec2_client: boto3.client) -> list[dict[str, Any]]:
    logger.info("Collecting EC2 instance inventory...")
    paginator = ec2_client.get_paginator("describe_instances")
    instances: list[dict[str, Any]] = []

    for page in paginator.paginate():
        for reservation in page.get("Reservations", []):
            for instance in reservation.get("Instances", []):
                instances.append(
                    {
                        "InstanceId": instance.get("InstanceId"),
                        "InstanceType": instance.get("InstanceType"),
                        "State": instance.get("State", {}).get("Name"),
                        "AvailabilityZone": instance.get("Placement", {}).get("AvailabilityZone"),
                        "PublicIpAddress": instance.get("PublicIpAddress"),
                        "PrivateIpAddress": instance.get("PrivateIpAddress"),
                        "LaunchTime": instance.get("LaunchTime"),
                    }
                )

    logger.info("Collected %d EC2 instances", len(instances))
    return instances

from __future__ import annotations

import logging
from typing import Any

import boto3


logger = logging.getLogger(__name__)


def collect_s3_buckets(s3_client: boto3.client) -> list[dict[str, Any]]:
    logger.info("Collecting S3 bucket inventory...")
    response = s3_client.list_buckets()
    buckets = []

    for bucket in response.get("Buckets", []):
        bucket_name = bucket.get("Name")
        creation_date = bucket.get("CreationDate")
        region = None

        if bucket_name:
            try:
                location = s3_client.get_bucket_location(Bucket=bucket_name)
                region = location.get("LocationConstraint") or "us-east-1"
            except Exception:
                logger.warning("Unable to determine region for bucket %s", bucket_name)

        buckets.append(
            {
                "BucketName": bucket_name,
                "CreationDate": creation_date,
                "Region": region,
            }
        )

    logger.info("Collected %d S3 buckets", len(buckets))
    return buckets

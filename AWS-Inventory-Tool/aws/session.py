from __future__ import annotations

from typing import Optional

import boto3


def create_aws_session(
    region_name: Optional[str] = None,
    aws_access_key_id: Optional[str] = None,
    aws_secret_access_key: Optional[str] = None,
    profile_name: Optional[str] = None,
) -> boto3.Session:
    return boto3.Session(
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        profile_name=profile_name,
    )

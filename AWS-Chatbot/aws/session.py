from __future__ import annotations

import boto3
from boto3.session import Session
from typing import Optional


def create_aws_session(
    region_name: Optional[str] = None,
    aws_access_key_id: Optional[str] = None,
    aws_secret_access_key: Optional[str] = None,
    profile_name: Optional[str] = None,
) -> Session:
    return boto3.Session(
        region_name=region_name,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        profile_name=profile_name,
    )

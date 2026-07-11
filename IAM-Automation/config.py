from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv


@dataclass
class Config:
    aws_region: str | None
    aws_access_key_id: str | None
    aws_secret_access_key: str | None
    aws_profile: str | None

    @classmethod
    def load(cls, env_path: Path | str | None = None) -> "Config":
        if env_path is None:
            env_path = Path(".env")
        else:
            env_path = Path(env_path)

        if env_path.exists():
            load_dotenv(env_path)
        else:
            load_dotenv()

        aws_region = os.getenv("AWS_REGION")
        aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
        aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
        aws_profile = os.getenv("AWS_PROFILE")

        if not aws_profile and not aws_access_key_id and not aws_secret_access_key:
            aws_profile = None

        return cls(
            aws_region=aws_region,
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key,
            aws_profile=aws_profile,
        )

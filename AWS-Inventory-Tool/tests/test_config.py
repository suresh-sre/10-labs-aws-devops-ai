from pathlib import Path

import pytest

from config import Config


def test_load_missing_env(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text("AWS_REGION=us-east-1\n")
    with pytest.raises(RuntimeError, match="Missing required environment variables"):
        Config.load(env_path=env_file)


def test_load_with_all_vars(tmp_path: Path) -> None:
    env_file = tmp_path / ".env"
    env_file.write_text(
        "AWS_REGION=us-east-1\nAWS_ACCESS_KEY_ID=testkey\nAWS_SECRET_ACCESS_KEY=testsecret\nOUTPUT_DIR=output\n"
    )

    config = Config.load(env_path=env_file)

    assert config.aws_region == "us-east-1"
    assert config.aws_access_key_id == "testkey"
    assert config.aws_secret_access_key == "testsecret"
    assert config.output_dir == Path("output")

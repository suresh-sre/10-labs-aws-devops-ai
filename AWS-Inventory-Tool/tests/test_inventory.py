from unittest.mock import Mock

from inventory.ec2 import collect_ec2_instances
from inventory.rds import collect_rds_instances
from inventory.s3 import collect_s3_buckets


def test_collect_ec2_instances_empty():
    mock_client = Mock()
    mock_client.get_paginator.return_value.paginate.return_value = [{"Reservations": []}]

    result = collect_ec2_instances(mock_client)

    assert result == []


def test_collect_s3_buckets_empty():
    mock_client = Mock()
    mock_client.list_buckets.return_value = {"Buckets": []}

    result = collect_s3_buckets(mock_client)

    assert result == []


def test_collect_rds_instances_empty():
    mock_client = Mock()
    mock_client.get_paginator.return_value.paginate.return_value = [{"DBInstances": []}]

    result = collect_rds_instances(mock_client)

    assert result == []

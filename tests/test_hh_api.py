from src.hh_api import HH
from unittest.mock import patch


@patch("requests.get")
def test_head_hunter_api_requests():

    obj_api = HH('../Data/JsonFile.json')
    assert type(obj_api) is HH

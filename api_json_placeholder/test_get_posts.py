import pytest
import requests
from utils import get_urls
from utils.json_placeholder_requests import get_request
POSTS_URL = get_urls.ALL_POSTS


def test_get_all_posts_status_200():
    response = get_request(POSTS_URL)
    status_code = response.status_code
    print(response.json())
    print(status_code)
    assert status_code == 200


def test_get_posts_from_one_user():
    pass
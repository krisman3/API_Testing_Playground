import pytest

from utils.get_urls import POSTS_URL
from utils.json_placeholder_requests import get_request


@pytest.fixture
def get_posts_endpoint():
    def _call(params=None):
        response = get_request(POSTS_URL, params=params)
        return response, response.json()
    return _call
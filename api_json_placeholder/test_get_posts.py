import pytest
import requests
from utils import get_urls


def test_get_all_posts():
    print(get_urls.ALL_POSTS)
    response = requests.get(get_urls.ALL_POSTS, verify=False)
    data = response.json()
    status_code = response.status_code
    print(data)
    print(status_code)

    assert status_code == 200
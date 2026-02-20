import json
from utils import get_urls
from utils.json_placeholder_requests import get_request

POSTS_URL = get_urls.ALL_POSTS


def test_get_all_posts_status_200():
    response = get_request(POSTS_URL)
    list_of_posts = response.json()
    status_code = response.status_code
    assert status_code == 200
    assert list_of_posts[0]["id"] == 1  # Checking if there's a post with an ID of 1


def test_get_posts_from_one_user():
    payload = {"userId": 1}
    response = get_request(POSTS_URL, params=payload)
    data = response.json()
    assert len(data) == 10  # According to documentation - the number of posts from user 1 are 10

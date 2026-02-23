import pytest

from utils import get_urls
from utils.json_placeholder_requests import get_request
from utils.read_csv import csv_reader
from utils.get_paths import csv_title_file

POSTS_URL = get_urls.ALL_POSTS
title_csv_file = csv_reader(csv_title_file)

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

@pytest.mark.parametrize("title,id,status", title_csv_file)
def test_get_specific_post_with_title(title, id, status):
    payload = {"title":title}
    response = get_request(POSTS_URL, params=payload)
    data = response.json()
    assert data[0]['id'] == id
    assert response.status_code == status

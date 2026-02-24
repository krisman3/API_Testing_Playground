import pytest

from utils import get_urls
from utils.json_placeholder_requests import get_request
from utils.read_csv import csv_reader
from utils.get_paths import csv_title_file
from utils.get_paths import id_body_file
from utils.get_paths import number_data_file

POSTS_URL = get_urls.ALL_POSTS
title_csv_file = csv_reader(csv_title_file)
id_csv_file = csv_reader(id_body_file)
number_csv_file = csv_reader(number_data_file)


def test_get_all_posts_status_200():
    response = get_request(POSTS_URL)
    list_of_posts = response.json()
    status_code = response.status_code
    assert status_code == 200
    assert list_of_posts[0]["id"] == 1  # Checking if there's a post with an ID of 1


@pytest.mark.parametrize("userId,number,status", number_csv_file)
def test_get_all_posts_from_single_user(userId, number, status):
    payload = {"userId": userId}
    response = get_request(POSTS_URL, params=payload)



@pytest.mark.parametrize("id,body,status", id_csv_file)
def test_get_post_from_one_user(id, body, status):
    payload = {"id": int(id)}
    response = get_request(POSTS_URL, params=payload)
    data = response.json()
    actual_body = data[0]["body"]
    correct_content = True
    if body not in str(actual_body):
        correct_content = False
    assert correct_content == True  # According to documentation - the number of posts from user 1 are 10

@pytest.mark.parametrize("title,id,status", title_csv_file)
def test_get_specific_post_with_title(title, id, status):
    payload = {"title":title}
    response = get_request(POSTS_URL, params=payload)
    data = response.json()
    assert data[0]['id'] == int(id)
    assert response.status_code == status

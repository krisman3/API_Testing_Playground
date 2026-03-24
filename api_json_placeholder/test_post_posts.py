from utils.json_placeholder_requests import post_request
from utils.get_urls import ALL_POSTS
from utils.read_csv import csv_reader
from utils.get_paths import creating_resources_file
import pytest

resources_file = csv_reader(creating_resources_file)

@pytest.mark.parametrize("title,body,user_id", resources_file)
def test_single_resource_positive(title,body,user_id):
    payload = {'title': title, 'body': body, 'userId': int(user_id)}
    headers = {'Content-type': 'application/json', 'charset':'UTF-8'}
    response = post_request(params=payload, url=ALL_POSTS, headers=headers)
    assert response.status_code == 201



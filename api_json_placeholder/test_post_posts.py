from utils.json_placeholder_requests import post_request
from utils.get_urls import ALL_POSTS

def test_single_resource():
    payload = {'title': 'RedBull', 'body': 'Max Verstappen #3', 'userId': 69}
    headers = {'Content-type': 'application/json', 'charset':'UTF-8'}
    response = post_request(params=payload, url=ALL_POSTS, headers=headers)
    assert response.status_code == 201
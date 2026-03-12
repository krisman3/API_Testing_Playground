from venv import logger

import requests



def get_request(url, verify=False, **kwargs):
    logger.info("Starting a GET request...")
    response = requests.get(url, verify=verify, **kwargs)
    return response


def post_request(url, verify=False, **kwargs):
    logger.info("Starting a POST request...")
    response = requests.post(url, verify=verify, **kwargs)
    print(f"Req URL: {response.request.headers}")
    return response
from venv import logger

import requests



def get_request(url, verify=False, **kwargs):
    logger.info("Starting a GET request...")
    response = requests.get(url, verify=verify, **kwargs)
    logger.info(f"Req URL: {response.request.url}")
    return response

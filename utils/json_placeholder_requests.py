from venv import logger

import requests

def get_request(url, verify=False, params=None):
    logger.info("Starting a GET request...")
    response = requests.get(url, verify=verify)
    return response
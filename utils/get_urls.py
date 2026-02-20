from config.env_utils import load_config

BASE_URL = load_config("qa")
POSTS_ENDPOINT = "posts/"
ALL_POSTS = BASE_URL + POSTS_ENDPOINT

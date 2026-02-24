from config.env_utils import load_config
curr_config = load_config("qa")

BASE_URL = curr_config["base_url"]
POSTS_ENDPOINT = "posts/"
ALL_POSTS = BASE_URL + POSTS_ENDPOINT
POSTS_URL = ALL_POSTS

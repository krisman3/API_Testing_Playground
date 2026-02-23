from config.env_utils import load_config, BASE_DIR
from utils.get_urls import BASE_URL

curr_config = load_config("qa")

csv_title_file = BASE_DIR / "test_data" / "title_data.csv"
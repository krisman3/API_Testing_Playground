from config.env_utils import load_config, BASE_DIR

curr_config = load_config("qa")
csv_title_file = BASE_DIR / "test_data" / "title_data_positive.csv"
id_body_file = BASE_DIR / "test_data" / "id_data_positive.csv"
number_data_file = BASE_DIR / "test_data" / "number_posts_positive.csv"
import duckdb
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

URL = "https://huggingface.co/datasets/McAuley-Lab/Amazon-Reviews-2023/resolve/main/raw/review_categories/Gift_Cards.jsonl"

def load_reviews(max_samples: int):
    logger.info("Start downloading...")
    df = pd.read_json(URL, lines=True, nrows=max_samples)
    logger.info(f"Downloaded {len(df)} reviews")
    print(df.head())
    return df

if __name__ == "__main__":
    load_reviews(max_samples=1000)
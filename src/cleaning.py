import duckdb
import logging
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def clean_reviews(db_path: str):
    logger.info("Starting data cleaning...")
    conn = duckdb.connect(db_path)
    conn.execute("DROP TABLE IF EXISTS reviews_cleaned")
    conn.execute("""
        CREATE TABLE reviews_cleaned AS
        SELECT rating, title, text, parent_asin, timestamp, helpful_vote, verified_purchase
        FROM reviews
        WHERE rating <= 2
        AND LENGTH(text) > 10
    """)
    count = conn.execute("SELECT COUNT(*) FROM reviews_cleaned").fetchone()[0]
    logger.info(f"Cleaned data: {count} negative reviews saved")
    conn.close()

if __name__ == "__main__":
    clean_reviews(db_path='data/reviews.duckdb')
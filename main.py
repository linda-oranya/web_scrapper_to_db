from database.write_to_db import write_csv_to_db
from scraper.data_scraper import scrape, clean_df, df_to_csv
from scraper.categories import categories


def main() -> None:
    NR_ITEMS_TO_SCRAPE = 3000

    for category in categories:
        scraped_df = scrape(category, NR_ITEMS_TO_SCRAPE)
        cleaned_df = clean_df(scraped_df)
        df_to_csv(cleaned_df, f"results/{category}")
        #write_csv_to_db(clean_df)
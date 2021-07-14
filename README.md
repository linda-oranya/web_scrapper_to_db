### Web Scrapper

This is a web scrapping project that scrapes from an ecommerce website (Etsy) and saves to database.
This website sells different varieties of items, we will be accessing individual items by keyword and scrape the:
        - title
        - price
        - image url
        - item url

The database, etsydata - where the data is pushed to- is hosted on Heroku.

The project contains the:

`data_scrapper.py` - For scrapping data

`write_to_db.py` - For writing data to db



### Installation

```pip install bs4```

```pip install request```

### Usage
The `datascrapper.py` takes in 2 parameters, the keyword/item you want to scrape and the number of rows you want to scrape

The maximum number of items on an etsy page is 64, hence, you must scrape 64 and above.

The `write_to_db.py` file requires a write access to  db

#### Sample code

```scrape_data('electronics',3000)```

### Development
The project is currently completed but open to modifications

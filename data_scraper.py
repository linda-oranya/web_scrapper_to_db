
import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import Union



def scrape(keyword_to_search:str,number_of_items_to_scrape:int):
    """
        Scrape data based on keyword and number of rows to be scrapped
    
        Parameters:
        keyword_to_search: The keyword that needs to be searched
        number_of_items: number of examples to be scraped
    """
    
    titles = []
    prices = []
    item_url = []
    images = []


    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
        "Accept-Encoding":"gzip, deflate", 
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
        "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"
    }
    
    page_number = int(round(number_of_items_to_scrape/64))
    print(f'Scrapping {page_number} pages')
    
    for i in range(1,page_number+1):
        print(i)
        url = f'https://www.etsy.com/ca/search?q={keyword_to_search}&page={i}&ref=pagination'
        r = requests.get(url,headers=headers)
        if r.status_code == 200:

            content = r.content
            soup = BeautifulSoup(content,"lxml")
               
            for title in soup.find_all("h3", class_="wt-mb-xs-0"):
                titles.append(title.text.strip())

        
            for price in soup.find_all("span",class_="currency-value"):
                prices.append(price.text)
            
        
            links = [a["href"] for a in soup.find_all("a", href=True)]
            for link in links:
                if link.startswith("https://www.etsy.com/ca/listing/"):
                    item_url.append(link)       
            
            
            for image in soup.find_all("img"):
                images.append(image.get('src'))  

                        
        else:
            print('page does not exist')

        dict_of_scrapped_items ={
            'title':titles,
            'price(CAD)':prices,
            'item_url':item_url,
            'image_url':images,
        }

        df = pd.DataFrame.from_dict(dict_of_scrapped_items, orient='index')
        df = df.transpose()
        df['category'] = keyword_to_search
        
    return df

def clean_df(df):
    """
        clean dataframe and export to csv

        Parameters:
        .csvfile

    """
    df.dropna(inplace=True)
    return df

def df_to_csv(df,filename): 
    """
        writes data to csv

        Parameters:
        df: Data to write to csv
        filename: csv name

    """ 
    df.to_csv(filename,index=False)


df = scrape('home',1000)
file = clean_df(df)
print(file)

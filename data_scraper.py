
import requests
from bs4 import BeautifulSoup
import pandas as pd
from typing import Union

class Scraper:
    """
        This class scrapes data from an ecommerce database, https://www.etsy.com/

        
    """

    def validate_input(keyword,number):
        """Validates input"""
        
        if isinstance(keyword,str) and isinstance(number,int):
            return True
        else:
            return False

    def scraper(keyword_to_search:str,number_of_items_to_scrape:int):
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
        print(page_number)
        
        for i in range(1,page_number+1):
            print(i)
            url = f'https://www.etsy.com/ca/search?q={keyword_to_search}&page={i}&ref=pagination'
            r = requests.get(url,headers=headers)
            if r.status_code == 200:

                content = r.content
                soup = BeautifulSoup(content,"lxml")
                try:   
                    for title in soup.find_all("h3", class_="wt-mb-xs-0"):
                        titles.append(title.text.strip())

                except AttributeError:
                    titles.append("")
                try:
                    for price in soup.find_all("span",class_="currency-value"):
                        prices.append(price.text)
                except:
                    prices.append("")
            
                try:
                    links = [a["href"] for a in soup.find_all("a", href=True)]
                    for link in links:
                        if link.startswith("https://www.etsy.com/ca/listing/"):
                            item_url.append(link)       
                except:
                    item_url.append("")
                try:
                    for image in soup.find_all("img"):
                        images.append(image.get('src'))
                except:
                    images.append("")   

                          
            else:
             print ('page does not exist')
            a ={
                'title':titles,
<<<<<<< HEAD
                'price(CAD)':prices,
=======
                'price':prices,
>>>>>>> a70d840fc996758f5dd5473385df5ae70e8d6ea2
                'item_url':item_url,
                'image_url':images,
            }
            df = pd.DataFrame.from_dict(a, orient='index')
            df = df.transpose()
            df['category'] = keyword_to_search
            
        return df

<<<<<<< HEAD
    def clean_df(df,filename):
        """
         clean dataframe and export to csv
        """
        df.dropna(inplace=True)
        df.to_csv(filename,index=False)


    df = scraper('home',10000)
    file = clean_df('home_data.csv')
=======
    def to_csv(df,filename):
        df.to_csv(filename,index=False)



    df = scraper('home',10000)
    file = to_csv('home_data.csv')
>>>>>>> a70d840fc996758f5dd5473385df5ae70e8d6ea2

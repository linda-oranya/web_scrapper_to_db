import pandas as pd
from io import StringIO
from sqlalchemy import create_engine


def get_csv(data):
    """
        Gets scrapped data saved in csv and converts to Pandas DataFrame
        
        Parameter:
            .csv file
    """
    df = pd.read_csv(data)
    return df

def write_csv_to_db(df):
    """
        writes csv file to database after authentication

        Parameter:
        df: Pandas DataFrame
    """
    
    engine = create_engine('postgresql://user:password@localhost/database')
    df.to_sql("home", engine)


df = get_csv('data.csv')

write_csv_to_db(df)

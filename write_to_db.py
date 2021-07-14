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

def db_csv_writer(df):
    """
        writes csv file to database after authentication

        Parameter:
        df: Pandas DataFrame
    """
    df.columns = [c.lower() for c in df.columns] #postgres doesn't like capitals or spaces

    
    engine = create_engine('postgresql://user:password@localhost/database')
    df.to_sql("home", engine)


df = pd.read_csv('data.csv')

db_csv_writer(df)

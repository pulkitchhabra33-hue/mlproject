import os
import pandas as pd
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

host= os.getenv("host")
user= os.getenv("user")
password= os.getenv("password")
db= os.getenv("db")

def read_sql_data():
    logging.info("Reading SQL database started")

    try:
        engine= create_engine(f"mysql+pymysql://{user}:{password}@{host}/{db}")

        logging.info("SQLAlchemy engine created successfully")
        query= 'Select * from students_performance'

        df= pd.read_sql_query(query, engine)
        print(df.head())
        
        logging.info("Reading SQL database completed")
        return df
    
    except Exception as ex:
        raise CustomException(ex, sys)
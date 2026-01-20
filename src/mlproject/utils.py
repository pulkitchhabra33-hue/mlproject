import os
import pandas as pd
import sys
from src.mlproject.exception import CustomException
from src.mlproject.logger import logging
from dotenv import load_dotenv
from sqlalchemy import create_engine
import pickle

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

def save_object(file_path, obj):
    try:
        dir_path= os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok= True)

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

    except Exception as e:
        raise CustomException(e, sys)
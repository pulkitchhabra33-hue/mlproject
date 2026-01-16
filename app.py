from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion

import sys

if __name__== "__main__":
    logging.info("Application has started")

    try:
        data_ingestion= DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.error("Application has failed", exc_info= True)
        raise CustomException(e, sys)
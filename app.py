from src.mlproject.logger import logging
from src.mlproject.exception import CustomException
from src.mlproject.components.data_ingestion import DataIngestion
from src.mlproject.components.data_transformation import DataTransformation, DataTransformationConfig
from src.mlproject.components.model_trainer import ModelTrainerConfig, ModelTrainer
import sys

if __name__== "__main__":
    logging.info("Application has started")

    try:
        #data ingestion
        data_ingestion= DataIngestion()
        train_data_path, test_data_path= data_ingestion.initiate_data_ingestion()

        #data transformation
        data_transformation= DataTransformation()
        train_array, test_array, _= data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        
         ## Model Training
        model_trainer=ModelTrainer()
        print(model_trainer.initiate_model_trainer(train_array, test_array))

    except Exception as e:
        logging.error("Application has failed", exc_info= True)
        raise CustomException(e, sys)
from src.logger import logger
from src.exception import CustomException
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer

if __name__=='__main__':
    try:
        # Data Ingestion
        logger.info('Starting data ingestion...')
        data_ingestion = DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
        logger.info(f"Train data path: {train_data_path}")
        logger.info(f"Test data path: {test_data_path}")

        # Data Transformation
        logger.info('Starting data transformation...')
        data_transformation = DataTransformation()
        train_arr, test_arr, _ = data_transformation.initiate_data_transformation(train_data_path, test_data_path)
        logger.info('Data transformation complete.')

        # Model Training
        logger.info('Starting model training...')
        model_trainer = ModelTrainer()
        model_trainer.initiate_model_training(train_arr, test_arr)
        logger.info('Model training complete.')

    except CustomException as e:
        logger.error("CustomException occurred during the training pipeline execution", exc_info=True)
    except Exception as e:
        logger.error("An unexpected exception occurred during the training pipeline execution", exc_info=True)

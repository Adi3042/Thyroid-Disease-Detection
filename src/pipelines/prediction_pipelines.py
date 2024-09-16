import sys
import os
import pandas as pd
from src.exception import CustomException
from src.logger import logger
from src.utils import load_object

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            # Define paths to preprocessor and model files
            preprocessor_path = os.path.join('artifacts', 'preprocessor.pkl')
            model_path = os.path.join('artifacts', 'model.pkl')

            # Load preprocessor and model
            preprocessor = load_object(preprocessor_path)
            model = load_object(model_path)

            # Preprocess and predict
            data_scaled = preprocessor.transform(features)
            pred = model.predict(data_scaled)
            return pred
        except Exception as e:
            logger.error("Exception occurred in prediction pipeline")
            raise CustomException(e, sys)

class CustomData:
    def __init__(self,
                 age: int,
                 sex: str,
                 lithium: str,
                 goitre: str,
                 psych: str,
                 T3: float,
                 T4U: float,
                 FTI: float,
                 tumor: str,
                 on_thyroxine: str,
                 hypopituitary: str,
                 on_antithyroid_medication: str,
                 thyroid_surgery: str,
                 I131_treatment: str):
        
        self.age = age
        self.sex = sex
        self.lithium = lithium
        self.goitre = goitre
        self.psych = psych
        self.T3 = T3
        self.T4U = T4U
        self.FTI = FTI
        self.tumor = tumor
        self.on_thyroxine = on_thyroxine
        self.hypopituitary = hypopituitary
        self.on_antithyroid_medication = on_antithyroid_medication
        self.thyroid_surgery = thyroid_surgery
        self.I131_treatment = I131_treatment

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'age': [self.age],
                'sex': [self.sex],
                'lithium': [self.lithium],
                'goitre': [self.goitre],
                'psych': [self.psych],
                'T3': [self.T3],
                'T4U': [self.T4U],
                'FTI': [self.FTI],
                'tumor': [self.tumor],
                'on_thyroxine': [self.on_thyroxine],
                'hypopituitary': [self.hypopituitary],
                'on_antithyroid_medication': [self.on_antithyroid_medication],
                'thyroid_surgery': [self.thyroid_surgery],
                'I131_treatment': [self.I131_treatment]
            }
            df = pd.DataFrame(custom_data_input_dict)
            logger.info('Dataframe gathered successfully')
            return df
        except Exception as e:
            logger.error('Exception occurred prediction pipeline while gathering dataframe')
            raise CustomException(e, sys)

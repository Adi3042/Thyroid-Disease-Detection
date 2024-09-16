import os
import sys
import pickle
from src.exception import CustomException
from src.logger import logging
from sklearn.metrics import r2_score, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

    
def save_object(file_path, obj):
    """
    Save an object to a file.
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as file_obj:
            pickle.dump(obj, file_obj)
    except Exception as e:
        logging.error("Exception occurred while saving object", exc_info=True)
        raise CustomException(e, sys)
    
def evaluate_model(X_train, y_train, X_test, y_test, models):
    """
    Evaluate multiple models and return their performance metrics.
    """
    try:
        report = {}
        for name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            acc = accuracy_score(y_test, y_pred)
            precision = precision_score(y_test, y_pred, average='weighted')
            recall = recall_score(y_test, y_pred, average='weighted')
            f1 = f1_score(y_test, y_pred, average='weighted')
            roc_auc = roc_auc_score(y_test, model.predict_proba(X_test), multi_class='ovr')
            report[name] = roc_auc
            logging.info(f'{name} - Accuracy: {acc:.2f}, Precision: {precision:.2f}, Recall: {recall:.2f}, F1 Score: {f1:.2f}, ROC AUC Score: {roc_auc:.2f}')
        return report
    except Exception as e:
        logging.error('Exception occurred during model evaluation', exc_info=True)
        raise CustomException(e, sys)
    
def load_object(file_path):
    """
    Load an object from a file.
    """
    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)
    except Exception as e:
        logging.error("Exception Occured in load_object function utils", exc_info=True)
        raise CustomException(e, sys)
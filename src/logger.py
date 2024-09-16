import logging
import os
from datetime import datetime
from logging.handlers import RotatingFileHandler

current_date = datetime.now().strftime('%Y/%m/%d')
log_directory = os.path.join(os.getcwd(), "logs", current_date)
os.makedirs(log_directory, exist_ok=True)

log_filename = datetime.now().strftime('%H_%M_%S') + '.log'
log_file_path = os.path.join(log_directory, log_filename)

formatter = logging.Formatter(
    '[ %(asctime)s ] %(levelname)s [%(name)s:%(lineno)d] - %(message)s'
)

rotating_handler = RotatingFileHandler(
    log_file_path,
    maxBytes=10**6,  
    backupCount=5    # Keep 5 old log files
)
rotating_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(logging.INFO)
logger.addHandler(rotating_handler)
logger.addHandler(console_handler)

logger.info("Logging setup is complete.")

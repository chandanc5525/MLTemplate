import os  # Managing files and directories related to your dataset, model checkpoints, logs
import sys # Accessing command-line arguments or controlling the execution environment of your script
import logging #  Recording important information, warnings, errors, and other messages during the execution of your machine learning code 
from datetime import datetime


LOG_FILE =  f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path = os.path.join(os.getcwd(),'logs',LOG_FILE)

os.makedirs(log_path,exist_ok = True)

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO
    
    
)

#if __name__ == '__main__':
#    logging.info('Logging Started')
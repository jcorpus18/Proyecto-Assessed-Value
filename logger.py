
import logging
import os
from datetime import datetime

# Directorios para logs
LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
EXC_DIR = os.path.join(os.path.dirname(__file__), 'exceptions')

os.makedirs(LOG_DIR, exist_ok=True)
os.makedirs(EXC_DIR, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'execution_logs.log'),
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_exception(exception):
    exc_file = os.path.join(EXC_DIR, 'exception_logs.log')
    with open(exc_file, 'a') as file:
        file.write(f"{datetime.now()} - EXCEPTION - {repr(exception)}\n")

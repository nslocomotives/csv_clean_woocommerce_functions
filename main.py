"""Main function to import csv data and push it into woocommerce api"""

import base64
import ast
import logging
import logging.handlers
from decouple import config
from google.cloud import secretmanager

#setting up loggers
logger = logging.getLogger('csvFucntions')
logger.setLevel(logging.DEBUG)

fh = logging.handlers.RotatingFileHandler(
    config(
        'LOGGING_LOCATION',
        default='/var/log/csvFunctions.log'
        ),
    maxBytes=10240,
    backupCount=5
    )
fh.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)

ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)
ch.setFormatter(formatter)

logger.addHandler(fh)
logger.addHandler(ch)

def unpack_data(data):
    """Function to unpack data from its encoded form"""
    result = ""
    result = base64.b64decode(data).decode('utf-8')
    result = ast.literal_eval(result)
    return result

def get_csv_data(payload):
    """Function to get a CSV and perform basic Validation"""
    result = {}
    result['error'] = False
    return result

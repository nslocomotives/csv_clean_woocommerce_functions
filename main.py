"""Main function to import csv data and push it into woocommerce api"""

import base64
import ast
import logging
import hashlib
import csv
import requests
import pandas as pd
import logging.handlers
from decouple import config
from google.cloud import secretmanager
from urllib.error import HTTPError
from pandas.errors import EmptyDataError

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

def catch_error_detail(e, attribute):
    if hasattr(e, attribute) is True:
        value = getattr(e, attribute)
    else:
        value = hasattr(e, attribute)
    return value

def get_csv_data(payload):
    """Function to get a CSV and perform basic Validation"""
    result = {}
    result['error'] = False
    try:
        result['data'] = pd.read_csv(payload['file_url'], error_bad_lines=False)
    except HTTPError as e:
        result['error_code']    = catch_error_detail(e, 'code')
        result['error']         = catch_error_detail(e, 'msg')
    except (EmptyDataError):
        result['error_code']    = 1001
        result['error']         = 'No columns to parse from file'
    return result

def check_file_updated(payload):
    """Checks the csv is different"""
    result = {}
    result['error'] = False
    result['file_changed'] = True
    with open(payload['file_path'], 'rb') as fh:
        md5hash = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            md5hash.update(data)
        result['file_hash'] = md5hash.hexdigest()
    remote_file = requests.get(payload['remote_file_url'], stream=True)
    md5hash = hashlib.md5()
    for data in remote_file.iter_content(8192):
        md5hash.update(data)
        result['remote_file_hash'] = md5hash.hexdigest()

    if result['file_hash'] == result['remote_file_hash']:
        result['file_changed'] = False
    else:
        result['file_changed'] = True

    print(result)


    return result

import base64
import logging
import logging.handlers
from decouple import config
from google.cloud import secretmanager

def unpack_data(data):
    """Function to unpack data from its encoded form"""
    result = ""
    result = base64.b64decode(data).decode('utf-8')
    # TODO: what is this eval doing?  there should be a better way to do this in python. # pylint: disable=W0511
    result = ast.literal_eval(result) #pylint disable:W0123
    return result

def get_csv_data(payload):
    '''Function to get a CSV and perform basic falidation'''
    result = {}
    results['error'] = False
    return result

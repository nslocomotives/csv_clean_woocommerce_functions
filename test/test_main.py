"""Unit tests for the main script"""

import base64
from decouple import config
from main import get_csv_data, unpack_data

# set static credentials variables
temptations_image_bank_user     = config('TEMPTAIONS_IMG_BNK_USR')
temptations_image_bank_password = config('TEMPTAIONS_IMG_BNK_PWD')
temptations_website_user        = config('TEMPTATIONS_WWW_USR')
temptations_website_password    = config('TEMPTATIONS_WWW_PWD')
wocommerce_url                  = config('WOOCOMERCE_URL')
wocommerce_ck                   = config('WOOCOMMERCE_CK')
wocommerce_cs                   = config('WOOCOMMERCE_CS')

def test_get_csv_data_success() -> None:
    """testing ability to collect csv file """
    payload = {}
    payload['file_url']         = 'https://github.com/nslocomotives/'
    payload['website_user']     = temptations_website_user
    payload['website_password'] = temptations_website_password

    results = get_csv_data(payload)
    assert results['error'] is False
    assert results['data'] is True

def test_get_csv_data_filenotfound() -> None:
    '''testing file not found error'''
    payload = {}
    payload['file_url']         = 'https://github.com/nslocomotives/'
    payload['website_user']     = temptations_website_user
    payload['website_password'] = temptations_website_password

    results = get_csv_data(payload)
    assert results['error'] == "File Not Found."

def test_get_csv_data_fileformaterror() -> None:
    '''testting file format of csv and correct handeling of error '''
    payload = {}
    payload['file_url']         = 'https://github.com/nslocomotives/'
    payload['website_user']     = temptations_website_user
    payload['website_password'] = temptations_website_password

    results = get_csv_data(payload)
    assert results['error'] == "File Format Error."

def test_unpack_data_with_encoded_data() -> None:
    '''testing unpacking base64 encoded data - expected use case'''
    message_data = {"file_name":"something.csv","wholesaler":"somesuplier"}
    data = base64.b64encode(str(message_data).encode('utf8'))
    unpacked_data = unpack_data(data)
    assert unpacked_data['file_name'] == message_data['file_name']
    assert unpacked_data['wholesaler'] == message_data['wholesaler']

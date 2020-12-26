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
    payload['file_url']         = 'https://raw.githubusercontent.com/nslocomotives/csv_clean_woocommerce_functions/master/test/testData/new_temptaions_AWIS.csv'
    payload['website_user']     = temptations_website_user
    payload['website_password'] = temptations_website_password

    results = get_csv_data(payload)
    assert results['error'] is False
    assert results['data'].empty is False

def test_get_csv_data_filenotfound() -> None:
    '''testing file not found error'''
    payload = {}
    payload['file_url']         = 'https://raw.github.com/nslocomotives/csv_clean_woocommerce_functions/blob/master/test/testData/notfound.csv'
    payload['website_user']     = temptations_website_user
    payload['website_password'] = temptations_website_password

    results = get_csv_data(payload)
    print(results)
    assert results['error'] == "Not Found"
    assert results['error_code'] == 404

def test_get_csv_data_fileformaterror() -> None:
    '''testting file format of csv and correct handeling of error '''
    payload = {}
    payload['file_url']         = 'https://raw.githubusercontent.com/nslocomotives/csv_clean_woocommerce_functions/master/test/testData/badformat.csv'
    payload['website_user']     = temptations_website_user
    payload['website_password'] = temptations_website_password

    results = get_csv_data(payload)
    assert results['error'] == "No columns to parse from file"
    assert results['error_code'] == 1001

def test_unpack_data_with_encoded_data() -> None:
    '''testing unpacking base64 encoded data - expected use case'''
    message_data = {"file_name":"something.csv","wholesaler":"somesuplier"}
    data = base64.b64encode(str(message_data).encode('utf8'))
    unpacked_data = unpack_data(data)
    assert unpacked_data['file_name'] == message_data['file_name']
    assert unpacked_data['wholesaler'] == message_data['wholesaler']

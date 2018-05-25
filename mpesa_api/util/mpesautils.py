from django.conf import settings
import base64
from mpesa_api.util.http import get
from openedx.core.djangoapps.site_configuration import helpers as configuration_helpers


def get_token(type):
    """
    fetch a new token
    :param: type: whether we are fetching token for B2C or C2B
    :return: JSON
    """

    url = configuration_helpers.get_value('GENERATE_TOKEN_URL', settings.GENERATE_TOKEN_URL)
    MPESA_C2B_ACCESS_KEY = configuration_helpers.get_value('MPESA_C2B_ACCESS_KEY', settings.MPESA_C2B_ACCESS_KEY)
    MPESA_C2B_ACCESS_KEY = configuration_helpers.get_value('MPESA_C2B_ACCESS_KEY', settings.MPESA_C2B_ACCESS_KEY)
    MPESA_B2C_ACCESS_KEY = configuration_helpers.get_value('MPESA_B2C_ACCESS_KEY', settings.MPESA_B2C_ACCESS_KEY)
    MPESA_B2C_CONSUMER_SECRET = configuration_helpers.get_value('MPESA_B2C_CONSUMER_SECRET',
                                                                settings.MPESA_B2C_CONSUMER_SECRET)
    concat_str = '{}:{}'.format(MPESA_C2B_ACCESS_KEY, MPESA_C2B_ACCESS_KEY)
    auth_token = encode_str_to_base_64(concat_str)
    if type.lower() == 'b2c':
        concat_str = '{}:{}'.format(MPESA_B2C_ACCESS_KEY, MPESA_B2C_CONSUMER_SECRET)
        auth_token = encode_str_to_base_64(concat_str)
    headers = {"Authorization": "Basic {}".format(auth_token)}
    response = get(url, headers)
    return response.json()


def encode_str_to_base_64(str_to_encode):
    """
    Encodes the a given string to base64
    :param str_to_encode: str to encode
    :return: base64 encoded str
    """
    return base64.urlsafe_b64encode(str_to_encode.encode('UTF-8')).decode('ascii')

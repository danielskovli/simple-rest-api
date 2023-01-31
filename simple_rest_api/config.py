'''App configuration'''

import os
from . import constants
from .models import host


class Environment:
    is_prod_server = os.getenv('FANCY_PROD_ENVIRONMENT')


class Security:
    api_key_numbytes = 32
    api_key_prefix = 'z_'

    class Hashing:
        api_key_method = constants.HashingMethod.sha256

    class Headers:
        api_key = 'Z-ApiKey'
        app_name = 'Z-AppName'

    class Query:
        api_key = 'z_apikey'
        app_name = 'z_appname'


class Hosts:
    pizza_sqlite = host.InMemorySqliteHost()


class RemoteEndpoints:
    wiki_random = 'https://en.wikipedia.org/api/rest_v1/page/random/summary'
    yr_forecast = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={lat:.3f}&lon={lon:.3f}'


class Tags:
    pizza = 'pizza'
    misc = 'miscellaneous'
    remote = 'remote'
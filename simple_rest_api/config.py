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
    pass


class Tags:
    pizza = 'pizza'
    misc = 'miscellaneous'
    remote = 'remote'
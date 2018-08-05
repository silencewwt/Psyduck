# -*- coding: utf-8 -*-

from bravado.client import SwaggerClient
from bravado.requests_client import RequestsClient
from BitMEXAPIKeyAuthenticator import APIKeyAuthenticator


class ProxyClient(RequestsClient):

    def __init__(self, proxies=None):
        super(ProxyClient, self).__init__()
        if proxies:
            self.update_proxies(proxies)

    def update_proxies(self, proxies):
        self.session.proxies.update(proxies)


def bitmex(config):
    swagger_config = {
        'use_models': False,
        'validate_responses': False,
        'also_return_response': True,
    }

    spec_url = config.HOST + config.SWAGGER_PATH
    client = ProxyClient(config.PROXIES)

    if config.api_key and config.api_secret:
        client.authenticator = APIKeyAuthenticator(
            config.HOST, config.API_KEY, config.API_SECRET
        )
    return SwaggerClient.from_url(
        spec_url, config=swagger_config, http_client=client
    )

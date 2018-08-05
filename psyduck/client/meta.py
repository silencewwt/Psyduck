# -*- coding: utf-8 -*-

from functools import wraps

from bravado.exception import HTTPError

from psyduck.client.exc import (
    RequestError
)


def request_deco(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            result = fn(*args, **kwargs)
        except HTTPError as exc:
            raise RequestError(exc.message)
        data, response = result
        return data
    return wrapper


class RequestMeta(type):

    def __new__(cls, name, bases, dct):
        for k, v in dct.items():
            if not k.startswith('__') and callable(v):
                dct[k] = request_deco(v)
        return type.__new__(cls, name, bases, dct)

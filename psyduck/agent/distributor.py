# -*- coding: utf-8 -*-

import json
from collections import namedtuple

from cfg import CONFIG
from psyduck.client import client
from psyduck.redis import cache_client


Instrument = namedtuple('Instrument', ['symbol', 'price', 'bid', 'ask'])


class Distributor(object):

    INSTRUMENT_CACHE_KEY = 'instrument:{}'

    @classmethod
    def get_instrument(cls, symbol):
        key = cls.INSTRUMENT_CACHE_KEY.format(symbol)
        value = cache_client.get(key)
        if value:
            return Instrument(*json.loads(value))
        return cls.get_active_instrument(symbol)

    @classmethod
    def get_active_instrument(cls, symbol):
        instruments = cls.pull_active_instruments()
        mapping = {i.symbol: i for i in instruments}
        return mapping.get(symbol)

    @classmethod
    def pull_active_instruments(cls):
        raw_items = client.get_instrument_active()
        instruments = list(map(cls.format_instrument, raw_items))
        cls.set_instruments_cache(instruments)
        return instruments

    @classmethod
    def set_instruments_cache(cls, instruments):
        pipe = cache_client.pipeline()
        for item in instruments:
            key = cls.INSTRUMENT_CACHE_KEY.format(item.symbol)
            pipe.set(key, json.dumps(item), CONFIG.REAL_TIME_EXPIRE)
        pipe.execute()

    @classmethod
    def format_instrument(cls, raw_item):
        return Instrument(
            symbol=raw_item['symbol'],
            price=raw_item['lastPrice'],
            bid=raw_item['bidPrice'],
            ask=raw_item['askPrice'],
        )

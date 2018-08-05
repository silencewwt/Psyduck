# -*- coding: utf-8 -*-

import cfg

from .client import bitmex
from .exc import RequestError
from .adapter import (
    BitmexAdapter,
)


raw_client = bitmex(cfg.CONFIG)
client = BitmexAdapter(raw_client)

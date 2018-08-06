# -*- coding: utf-8 -*-
from redis import Redis

import cfg

cache_client = Redis.from_url(cfg.CONFIG.REDIS_URI)

# -*- coding: utf-8 -*-
import os
import importlib


class Config(object):

    def __init__(self, c):
        self.config = c

    def __getattr__(self, item):
        return self.config.get(item, None)


name = os.getenv('PSYDUCK_CONFIG') or 'default'

config = importlib.import_module('cfg.{}'.format(name))
CONFIG = Config(config.CONFIG)

# -*- coding: utf-8 -*-

import logging
import config

_handler = logging.StreamHandler()
_formatter = logging.Formatter(config.LOG_FORMAT)
_handler.setFormatter(_formatter)

logger = logging.getLogger(config.LOGGER_NAME)
logger.addHandler(_handler)
logger.setLevel(logging.DEBUG)

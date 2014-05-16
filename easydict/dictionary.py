# -*- coding: utf-8 -*-

import json

from http import post
from . import config
from .logger import logger

def get_result_by_keyword(keyword):
  TRANSLATE_URL = config.TRANSLATE_URL
  HEADERS = config.HEADERS
  data = dict(i=keyword)
  data.update(config.TRIVAL_DATA)
  result = post(url=TRANSLATE_URL, headers=HEADERS, data=data)
  result = json.loads(result)
  for key in (u'elapsedTime', u'errorCode', u'type'):
    del result[key]
  return result

# -*- coding: utf-8 -*-

import threading
import json

import config
from logger import logger
from http import post

def get_result_by_keyword(keyword):
  TRANSLATE_URL = config.TRANSLATE_URL
  HEADERS = config.HEADERS
  data = dict(i=keyword)
  data.update(config.TRIVAL_DATA)
  result = post(url=TRANSLATE_URL, headers=HEADERS, data=data)
  try:
    result = json.loads(result)
  except:  
    return None
  for key in (u'elapsedTime', u'errorCode', u'type'):
    del result[key]
  return result

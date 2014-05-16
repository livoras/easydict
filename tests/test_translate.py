# -*- coding: utf-8 -*-
from easydict.logger import logger

from easydict import dictionary
def test_get_translate_data():
  data = dictionary.get_result_by_keyword('hello')
  assert u'hello' in str(data)

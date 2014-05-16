# -*- coding: utf-8 -*-

TRANSLATE_URL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict.top'

HEADERS = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-Encoding': 'gzip,deflate,sdch',
  'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'Connection': 'keep-alive',
  'Host': 'fanyi.youdao.com',
  'Origin': 'http://fanyi.youdao.com',
  'Referer': 'http://fanyi.youdao.com/translate?i=easydict&keyfrom=dict.top',
  'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.132 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
}

LOGGER_NAME = 'easydict'

LOG_FORMAT = "%(levelname)s :: %(asctime)s :: %(name)s :: %(message)s"

TRIVAL_DATA = dict(
  type='AUTO',
  doctype='json',
  xmlVersion='1.6',
  keyfrom='fanyi.web',
  ue='UTF-8',
  typoResult='true'
)

# -*- coding: utf-8 -*-

import urllib2
import urllib
import gzip
from StringIO import StringIO

from .logger import logger

def post(url, headers={}, data={}):
  data = urllib.urlencode(data)
  req = urllib2.Request(url=url, headers=headers, data=data)
  res = urllib2.urlopen(req)

  # Because the content encoding of the fucking youdao is `gzip`,
  # if you use `res.read()` directly you will get a binary data  
  # From stackoverflow, I got this resolution: 
  #   http://stackoverflow.com/questions/3947120/does-python-urllib2-automatically-uncompress-gzip-data-fetched-from-webpage
  if res.info().get('Content-Encoding') == 'gzip':
    buf = StringIO(res.read())
    f = gzip.GzipFile(fileobj=buf)
    result = f.read()
  else:  
    result = res.read()

  return result

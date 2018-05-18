#!/usr/local/bin/python2
# _* coding: utf-8 _*_

import urllib2

url = "http://www.baidu.com"

request = urllib2.Request(url)

response = urllib2.urlopen(request)

print response.read()
#!/usr/local/bin/python2
# _* coding: utf-8 _*_

import urllib
import urllib2

url = "http://www.baidu.com/s"
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

keyword = raw_input("请输入需要查询的字符串：")

wd = {"wd":keyword}

# 通过urllib.urlencode()参数是一个dict类型
wd = urllib.urlencode(wd)

# 拼接完整的url
fullurl = url + "?" + wd

# 构造请求对象
request = urllib2.Request(fullurl,headers = headers)

response = urllib2.urlopen(request)

print response.read()
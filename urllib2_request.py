#!/usr/local/bin/python2
# _* coding: utf-8 _*_

import urllib2

# User-Agent 是爬虫和反爬虫斗争的第一步
ua_headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"

}
# 通过urllib2.Request() 方法构造一个请求对象
request = urllib2.Request("http://www.baidu.com/", headers = ua_headers)

# 向指定的url地址发送请求病返回服务器响应的类文件对象
response = urllib2.urlopen(request)

# 服务器返回的类文件对象支持Python文件对象的操作方法
# read()方法就是读取文件里的全部内容，返回字符串

html = response.read()

# 打印响应内容
print html

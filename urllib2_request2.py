#!/usr/local/bin/python2
# _* coding: utf-8 _*_

import urllib2
import random

url = "http://www.baidu.com"

# 可以是User-Agent列表，也可以是代理列表
ua_list = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50",
    "Opera/8.0 (Windows NT 5.1; U; en)"
]

# 在User-Agent列表里随机选择一个User-Agent
user_agent = random.choice(ua_list)

# 构造一个请求
request = urllib2.Request(url)

# add_header()方法，添加/修改 一个HTTP报头
request.add_header("User-Agent", user_agent)

# get_header()获取一个已有的HTTP报头的值，注意只能是一个字母大写，其他的必须小写
print request.get_header("User-agent")
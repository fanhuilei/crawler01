#!/usr/local/bin/python2
# _* coding: utf-8 _*_

import urllib
import urllib2

url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%88%B1%E6%83%85&sort=recommend"

headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"}

formdata = {
    "page_limit": "20",
    "page_start": "0"
}

data = urllib.urlencode(formdata)

request = urllib2.Request(url,data=data,headers=headers)

print urllib2.urlopen(request).read()
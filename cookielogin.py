#!/usr/local/bin/python2
# _* coding: utf-8 _*_

import urllib2

url = "http://www.renren.com/470137425/profile"

headers = {
    "Host":"www.renren.com",
    "Connection": "keep-alive",
    #"Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "http://www.renren.com/SysHome.do",
    #"Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "anonymid=jhbripcz-h5snww; depovince=JX; jebecookies=22a803d5-eca9-43a1-ac06-6be4ea702c37|||||; _r01_=1; JSESSIONID=abckwACJvxlyQ4XDsLYnw; ick_login=d48b7217-3610-462a-b7b6-a90f053146ab; _de=4ED0D816D96743EA3EAE85F9536018E0; p=bbea6aeb59d750f822fbe0c40ec4472f5; first_login_flag=1; ln_uact=13818090781; ln_hurl=http://hdn.xnimg.cn/photos/hdn521/20150727/1135/main_6FH7_725c0000155f195a.jpg; t=66aec342793499cf8ec71187570c0f475; societyguester=66aec342793499cf8ec71187570c0f475; id=470137425; xnsid=8d6a684e; loginfrom=syshome; ch_id=10016; jebe_key=c06488b2-9607-4fdb-ad0c-d8dec5272801%7C09ba35fcdded49efb0f24861edd6619f%7C1526635798880%7C1%7C1526635800465; wp_fold=0"
}
request = urllib2.Request(url, headers=headers)

response = urllib2.urlopen(request)

print response.read()
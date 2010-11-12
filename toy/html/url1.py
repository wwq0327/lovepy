#!/usr/bin/env python
#coding:utf-8

import urlparse

urlscheme = 'http'
urllocation = 'www.python.org'
urlpath = 'lib/module-urlparse.html'

modList = ('urllib',
           'urllib2',
           'httplib',
           'cgilib'
           )

print "用Google搜索Python时地址栏中URL的解析结果"
parsedTuple = urlparse.urlparse(
    "http://www.google.com.hk/search?hl=en&q=urlparse&btnG=Google+Search"
    )
print parsedTuple

print "\t反解析Ptyhon文档页面的URL"
unparsedURL = urlparse.urlunparse(
    (urlscheme,
     urllocation,
     urlpath,
     '',
     '',
     '')
    )
print "\t"+unparsedURL
print "\n利用拼接方式添加更多Python文档页面的URL"

for mod in modList:
    newurl = urlparse.urljoin(unparsedURL,
    "module-%s.html" % mod)
    print "\t"+newurl
newurl = urlparse.urljoin(unparsedURL,
                          "module-urllib2/request-objects.html")
print "\t"+newurl

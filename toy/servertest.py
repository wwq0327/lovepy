#!/usr/bin/env python
#coding:utf-8
#测试网址安全性

import urllib
import urllib2

def virus_total():
    url = 'http://virustotal.com/search.html'
    user_agent = 'Mozila/4.0 (compatible;MSIE 5.5;Windows NT)'
    values = {'chain':'www.python.org'}
    headers = {'User-Agent':user_agent}

    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)
    the_page = response.read()

if __name__ == '__main__':
    virus_total()

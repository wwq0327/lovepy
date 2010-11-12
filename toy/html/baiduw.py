#!/usr/bin/env python
#coding:utf-8

import urllib2
#import re
from HTMLParser import HTMLParser

#urlText = []
url = 'http://www.baidu.com/s?wd=%CC%EC%C6%F8'

def getPage(url):
    page = urllib2.urlopen(url)
    pageContent = page.read()
    page.close()
    return pageContent

class parseWeather(HTMLParser):
    def init_parse(self):
        self.pieces = []

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            for k, v in attrs:
                if v == 'al_tr':
                    self.pieces.append(v)

    def handle_endtag(self, tag):
        if tag == 'td':
            self.pieces.append("%s"%(tag))

    def handle_data(self, data):
        if data != "\n":
            self.pieces.append(data.decode('gbk').encode('utf-8'))
            
def main():
    w = parseWeather()
    w.init_parse()
    htmlsource = getPage(url)
    w.feed(htmlsource)
    for item in w.pieces:
        print item


if __name__ == '__main__':
    main()

#htmlpage = getPage(url)
#getWeather(htmlpage)

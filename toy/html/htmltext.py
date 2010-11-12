#!/usr/bin/env python
#coding:utf-8
import HTMLParser
import urllib
urlText = []

class parseText(HTMLParser.HTMLParser):
    def handle_data(self, data):
        if data !="\n":
            urlText.append(data)

IParser = parseText()
IParser.feed(urllib.urlopen('http://docs.python.org/lib/module-HTMLParser.html').read())

IParser.close()
for item in urlText:
    print item

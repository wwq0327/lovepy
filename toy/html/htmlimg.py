#!/usr/bin/env python
#coding:utf-8

import HTMLParser
import urllib
import sys

#urlString = 'http://www.python.org'

def getImage(addr):
    '''
    将HTML解析成功的Images链接接收，并保存为图片
    '''
    u = urllib.urlopen(addr)
    data = u.read()
    splitPath = addr.split("/")
    fName = splitPath[-1]
    print "Saving %s" % fName
    f = open(fName, 'wb')
    f.write(data)
    f.close()

class parseImages(HTMLParser.HTMLParser):
    '''
    解析HTML文本，得到Image链接，并用getImage处理
    '''
    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for name, value in attrs:
                if name == 'src':
                    print 'V==>'+value
                    getImage(urlString+"/"+value)

def Usage(argv):
    if len(argv)==1:
        print '''
        Usage:\n\thtmlimg.py URL
        '''
        exit()
    else:
        url = argv[1]
        return url

if __name__ == '__main__':
    #创建实例
    IParser = parseImages()
    #打开链接
    urlString = Usage(sys.argv)
    u = urllib.urlopen(urlString)
    print "Opening URL\n====================="
    #info
    print u.info()
    #解析并下载图片
    IParser.feed(u.read())
    #退出
    IParser.close()

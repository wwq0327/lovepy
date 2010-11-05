#!/usr/bin/env python
#coding:utf-8

import os, sys, base64

def myargv(argv):
    if len(argv) == 2:
        url = argv[1]
        return url
    else:
        print 'Input Error! \nUsage: %s url' % (argv[0])
        sys.exit(1)

def convert(argv):
    url = myargv(argv)

    if url.startswith('thunder://'):
        url = url[10:]+'\n'
        url = base64.decodestring(url)
        url = url[2:-2]
    elif url.startswith('flashget://'):
        url = url[11:url.find('&')]+'\n'
        url = base64.decodestring(url)
        url = url[10:-10]
    elif url.startswith('qqdl://'):
        url = url[7:]+'\n'
        url = base64.decodestring(url)
    else:
        print '\n It is not a available url!!'
    return url

def downurl(url):
    os.system('wget '+url)
    
def test():
    p = convert(sys.argv)
    print p

if __name__ == '__main__':
    #test()
    p = convert(sys.argv)
    downurl(p)

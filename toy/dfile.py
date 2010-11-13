#!/usr/bin/env python
#coding:utf-8
#删除当前目录中的垃圾文件
#程序主要使用os类，index模块参考自PyUG关于os使用方法资料，
#精巧网址：http://goo.gl/5w9DP

import sys
import os

__author__ = 'wwq0327'

def index(directory):
    '''
    目录搜索，返回搜索到的文件
    '''
    stack = [directory]
    files = []
    while stack:
        directory = stack.pop()
        for file in os.listdir(directory):
            fullname = os.path.join(directory, file)
            files.append(fullname)
            if os.path.isdir(fullname) and not os.path.islink(fullname):
                stack.append(fullname)            
    return files

def delfile(dir):
    '''
    删除相应文件的操作。
    '''
    for file in index(dir):
        if os.path.splitext(file)[1] == '.py~':
            print '搜索到当前目录中含有.py~文件如：\n----------------------'
            filename = os.path.split(file)[1]
            print filename,
        else:
            print '真是太幸运了，程序末发现你当前目录中存在.py~文件,程序已自动退出'            
            sys.exit(1)
        
    s = raw_input('\n----------------------\n确定要删除以上文件吗？(y/[N]):')
    if s.lower() != 'y':
        print '操作结束，没有删除任何文件，程序将中止...'
        sys.exit(1)
    for delfile in index(dir):
        f = os.path.splitext(delfile)
        if f[1] == '.py~':
            os.remove(delfile)
    print '.py~ 已删除!程序就此退出！'

def Usage(argv):
    s = '''
    这是一个删除Emacs所产生.py~文件的程序。\n
    使用方法：python dfile.py\n
    '''
    if len(argv) > 1:
        print s
        sys.exit(1)
        
if __name__ == '__main__':
    dir = os.getcwd()
    argv = sys.argv
    Usage(argv)
    #print sys.argv
    print '当前工作目录是 %s' % dir
    delfile(dir)

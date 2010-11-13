#!/usr/bin/env python
#coding:utf-8

import sys
import os

def index(directory):
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
    print '搜索到当前目录中含有.py~文件如：\n----------------------'
    for file in index(dir):
        if os.path.splitext(file)[1] == '.py~':
            filename = os.path.split(file)[1]
            print filename,
    s = raw_input('\n--------------------\n确定要删除以上文件吗？(y/[N]):')

    if s.lower() != 'y':
        print '操作结束，没有删除任何文件，程序将中止...'
        sys.exit(1)
    for delfile in index(dir):
        f = os.path.splitext(delfile)
        if f[1] == '.py~':
            os.remove(delfile)
        print '.py 已删除!程序就此退出！'
        
if __name__ == '__main__':
    delfile('.')

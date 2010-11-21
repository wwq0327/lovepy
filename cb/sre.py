#!/usr/bin/env python
#coding:utf-8
#搜索并替换文件里的文字
#测试过了，很有效。

import os, sys
nargs = len(sys.argv)

if not 3 <= nargs <= 5:
    print "usage: %s s_text r_text [infile [outfile]]" % os.path.basename(sys.argv[0])
else:
    stext = sys.argv[1]
    rtext = sys.argv[2]
    input = sys.stdin
    output = sys.stdout
    if nargs >3:
        input_file = open(sys.argv[3])
    if nargs >4:
        output_file = open(sys.argv[4], 'w')
    for s in input_file:  #将文件当作一个字符串来读取。
        output_file.write(s.replace(stext, rtext))
    output.close()
    input.close()

#!/usr/bin/env python
#coding:utf-8
'''
本程意在自动化完成一些linux安装方面的命令。
'''
import os

#判断是否为Windows系统操作系统，如果是的话，则退出。
if os.name == 'nt':
    print '对不起，本程序只能在linux系统上运行，程序正在退出...'
    exit(0)
else:
    print "你当前使用的是 %s 操作系统，能使用本程序."%os.name

def cmdUsage():
    '''
    程序的使用方法：
    '''
    pass

def cmdRun(cmd):
    '''
    运行操作命令符
    '''
    os.system(cmd)

def cmdlog():
    '''将操作记录写入当前目录文件中。
    '''
    pass

def oschose():
    '''
    操作系统的选择，ubuntu或fedora,
    ubuntu:apt 方式安装
    fedora:yum 方式安装
    '''
    pass
def main():
    cmdresult = []
    cmdfile = open('command.conf','r')
    for cmdline in cmdfile.readlines():
        cmdline = cmdline.strip()
        if not len(cmdline) or cmdline.startswith('#'):
            #print cmdline
            continue
        print '''\n
        +========================＝＝＝＝＝===============
        |
        | 当前正在执行的操作是：%s
        |
        +============================＝===================
        '''%cmdline
        cmdRun(cmdline)
    #continue
    cmdresult.append(cmdline)

#open('cmd.log','w').write('%s'%'\n'.join(cmdresult))

if __name__ == '__main__':
    main()


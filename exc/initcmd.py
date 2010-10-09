#!/usr/bin/env python
#coding:utf-8
'''
本程意在自动化完成一些linux安装方面的命令。
用于安装的命令集合，在连接时可从终中下载。
'''
import sys
import os

#判断是否为Windows系统操作系统，如果是的话，则退出。
if os.name == 'nt':
    print '对不起，本程序只能在linux系统上运行，程序正在退出...'
    sys.exit(0)
else:
    print "你当前使用的是 %s 操作系统，能使用本程序."%os.name
    
def cmdUsage():
    '''
    程序的使用方法：
    python initcmd.py [-command]

    command:

    -h : 显示帮助。
    -d : 从网络中下载操作命令行。
    -p : 将命令行提交到作者邮箱。
    '''
    pass

def downcmdfile():
    '''
    从网站下载新的安装命令文件
    '''
    os.system('wget http://gopython.googlecode.com/files/cmds.tar.gz')
    os.system('tar -zxvf cmds.tar.gz')

def postcmdline():
    '''
    提交新的命令于，接收对象为作者邮箱。
    @TODO
    '''
    pass
    
#def cmdRun(cmd):
#    '''
#    运行操作命令符
#   '''
#    os.system(cmd)

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

def slupdate(oschose):
    '''根据所选的不同系统，作相应的更新操作,暂时只支持ubuntu和fedora'''
    if oschose == 'ubuntu':
        os.system('wget http://gopython.googlecode.com/files/sources.list')
        os.system('sudo mv /etc/apt/sources.list /etc/apt/sources.list.bak') 
        os.system('sudo cp sources.list /etc/apt/')
        os.system('sudo apt-get update')
    elif oschose == 'fedora':
        os.system('wget http://mirrors.163.com/.help/fedora-163.repo')

        os.system('wget http://mirrors.163.com/.help/fedora-updates-163.repo')
        os.system("su -c 'cp *.repo /etc/yum.repos.d/'")
        os.system("su -c 'yum makecache'")
        
    else:
        print '对不起，本程序暂时不支持ubuntu和fedora以外的系统。'

def runcmd(cmdfile):
    cmdresult = []
    cmdfile = open(cmdfile,'r')
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
        #cmdRun(cmdline)
        os.system(cmdline)
    #continue
    cmdresult.append(cmdline)

#open('cmd.log','w').write('%s'%'\n'.join(cmdresult))

def main():
    runcmd('command.conf')

if __name__ == '__main__':
    main()


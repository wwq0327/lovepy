#!/usr/bin/env python
#coding:utf-8

import sys
import os
import cmd

class pyCMD(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = "(pyCMD)"
        self.intro = '''pyCMD 使用说明：
        autocmd - 自动化命令安装开始。
        slist - 根据你所使用的系统，来更新你的软件源文件。
        initcmd - 手动向 command.conf　命令集合中添加你所需的命令行。
        recmd - 远程更新作者所提供的常用的安装命令。
        oschose - 选择你当前工作的操作系统，１～ ubuntu,2 ~ fedora
        EOF -　退出本程序
        help - cmd 显示各项帮助。
        '''

    def help_EOF(self):
        print "退出本程序 Quits the program"

    def do_EOF(self, line):
        sys.exit()

    def help_autocmd(self):
        print '开始更新你的系统...'

    def do_autocmd(self):
        os.system("ls -la")

    def help_slist(self):
        print '更新你的源...'

    def do_slist(self):
        pass

    def help_initcmd(self):
        print '向 command.conf中添加自定义命令'

    def do_initcmd(self):
        pass

    def help_recmd(self):
        print '远程更新你的安装命令集文件'

    def do_recmd(self):
        pass
    
    def help_oschose(self):
        print '选择你现所正在使用的系统.'

    def do_oschose(self):
        pass

if __name__ == "__main__":
    cmd = pyCMD()
    cmd.cmdloop()

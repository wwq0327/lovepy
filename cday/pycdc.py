#coding=utf-8
import sys, cmd
from cdctools import *

class PyCDC(cmd.Cmd):
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.CDROM = '/home/wyatt/lovepy/cday'
        self.CDDIR = 'cdc/'
        self.prompt='(PyCDC)>'
        self.intro='''PyCDC0.5使用说明'''

    def help_EOF(self):
        print "退出程序 Quits the program"

    def do_EOF(self, line):
        sys.exit()

    def help_walk(self):
        print "扫描光盘内容 walk cd and export into *.cdc"

    def do_walk(self,filename):
        if filename == "":
            filename = raw_input("输入cdc文件名::")
        print "扫描光盘内容保存到：'%s'" % filename
        #cdWalker(self.CDROM, self.CDDIR+filename)
        iniCDinfo(self.CDROM, "%s/%s"%(self.CDDIR,filename))
    def help_dir(self):
        print "指定保存/搜索目录"

    def do_dir(self, pathname):
        if pathname == "":
            pathname = raw_input("输入指定保存/搜索目录:")
        self.CDDIR = pathname
        print "指定保存/搜索目录:'%s' ;默认是：'%s'" % (pathname, self.CDDIR)

    def help_find(self):
        print "搜索关键词"

    def do_find(self, keyword):
        if keyword == "":
            keyword = raw_input("输入搜索关键词：")
        #print "搜索关键词：'%s'" % keyword
        cdcGrep(self.CDDIR, keyword)

if __name__ == '__main__':
    cdc = PyCDC()
    cdc.cmdloop()
    #CDROM = '/home/wyatt/gopython/cday/cdc'
    #cdWalker(CDROM, "cdc/cdctools.cdc")

#coding=utf-8
import os
import chardet
from ConfigParser import RawConfigParser as rcp

def iniCDinfo(cdrom, cdcfile):
    '''光盘信息.ini格式化函数
    @note: 直接利用os.walk()函数的输出信息由ConfigParser.RawConfigParser进行重组处理。
    @param cdrom:光盘访问目录
    @param cdcfile:输出的光盘信息记录文件路径
    @return:无，直接输出.ini文件
    '''

    walker = {}
    for root, dirs, files in os.walk(cdrom):
        walker[root]=(dirs, files)
    cfg = rcp()
    cfg.add_section("Info")
    cfg.add_section("Comment")
    cfg.set("Info",'ImagePaht',cdrom)
    cfg.set("Info",'Volume',cdcfile)
    cfg.set("Info",'FAT','CDFS')
    dirs = walker.keys()
    i=0
    for d in dirs:
        i+=1
        cfg.set("Comment",str(i),d)
    for p in walker:
        cfg.add_section(p)
        for f in walker[p][1]:
            cfg.set(p,f,os.stat("%s/%s"%(p,f)).st_size)
    cfg.write(open(cdcfile,"w"))


def cdWalker(cdrom, cdcfile):
    export = ""
    for root, dirs, files in os.walk(cdrom):
        #export += "\n %s;%s;%s" % (root, dirs, files)
        print formatCDinfo(root, dirs, files)
        export+=formatCDinfo(root, dirs, files)
    open(cdcfile, 'w').write(export)

def formatCDinfo(root, dirs, files):
    export = "\n"+root+"\n"
    for d in dirs:
        export+="-d "+root+_smartcode(d)+"\n"
    for f in files:
        export+= "-f %s %s \n"%(root, _smartcode(f))
    export += "="*70
    return export

def cdcGrep(cdcpath, keyword):
    filelist = os.listdir(cdcpath)
    for cdc in filelist:
        if ".cdc" in cdc:
            cdcfile= open(cdcpath+cdc)
            for line in cdcfile.readlines():
                if keyword in line:
                    print line

def _smartcode(stream):
    """smart recove stream into UTF-8
    """
    ustring = stream
    codedetect = chardet.detect(ustring)["encoding"]
    print codedetect
    try:
        print ustring
        ustring = unicode(ustring, codedetect)
        print ustring
        return "%s %s"%("",ustring.encode('utf8'))
    except:
        return u"bad unicode encode try!"

if __name__ == '__main__':
    CDROM = '/home/wwq/gopython'
    cdWalker(CDROM, 'cdc/cdctools.cdc')
    #cdcGrep('cdc/','bare.py')


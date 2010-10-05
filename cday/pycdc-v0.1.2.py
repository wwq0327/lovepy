#coding:utf-8
import os 

CDROM='/home/wyatt/lovepy/cday'

#print os.listdir("/home/wyatt/lovepy/cday")
for root, dirs, files in os.walk(CDROM):
    #print root, dirs, files
    open('mycdc.cdc','a').write("%s %s %s"%(root, dirs,files))

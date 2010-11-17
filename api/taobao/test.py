#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import time
import md5
from xml.dom import minidom
 
t = time.localtime()

paramArray = {
    'app_key':'test',
    'method':'taobao.taobaoke.items.get',
    'format':'xml',
    'v':'1.0',
    'timestamp':time.strftime('%Y-%m-%d %X', t),
    'fields':'iid,title,nick,pic_url,price,click_url,commission,\
              commission_rate,commission_num ,commission_volume ',
    'pid':'mm_5410_0_0',
    'cid':'1512',
    'page_no':'1',
    'page_size':'6'
}

def _sign(param,sercetCode):
    src = sercetCode + ''.join(["%s%s" % (k, v) for k, v in sorted(param.items())])
    return md5.new(src).hexdigest().upper()
 
# generate sign
sign = _sign(paramArray, 'test');
paramArray['sign'] = sign

form_data = urllib.urlencode(paramArray)
#print form_data

urlopen = urllib2.urlopen('http://gw.sandbox.taobao.com/router/rest', form_data)
 
rsp = urlopen.read();
xmldoc = minidom.parseString(rsp)

rsp = rsp.decode('UTF-8');
print rsp

# parse output
print "--------------------------------------------------------------------------------"
taobaokeItem = xmldoc.getElementsByTagName('taobaokeItem')
for i in range(0, taobaokeItem.length):
    #print taobaokeItem[i].toxml()
    print "###########################################"

    attr = taobaokeItem[i].attributes
    for (key, value) in attr.items():
        print key, "=>", value

    nodes = taobaokeItem[i].childNodes
    for j in range(0, nodes.length):
        name = nodes[j].nodeName
        value = nodes[j].childNodes[0].nodeValue
        print name, "=>", value

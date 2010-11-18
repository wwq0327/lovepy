# -*- coding: utf-8 -*-
##此代码片段的功能：查询手机类的淘客商品
import urllib
import urllib2
import string
import time
import md5
import re
import types
import logging
from xml.dom import minidom
 
 
#获得当前时间
t = time.localtime()
 
#参数数组
paramArray = {
	'app_key':'test',
	'method':'taobao.taobaoke.items.get',
	'format':'xml',
	'v':'1.0',
	'timestamp':time.strftime('%Y-%m-%d %X', t),
	'fields':'iid,title,nick,pic_url,price,click_url',
	'pid':'mm_5410_0_0',
  	'cid':'1512',
  	'page_no':'1',
  	'page_size':'6'
}
 
#签名函数
def _sign(param,sercetCode):
	src = sercetCode + ''.join(["%s%s" % (k, v) for k, v in sorted(param.items())])
	return md5.new(src).hexdigest().upper()
 
 
#生成签名
sign = _sign(paramArray, 'test');
paramArray['sign'] = sign
 
#组装参数
form_data = urllib.urlencode(paramArray)
 
#访问服务
urlopen = urllib2.urlopen('http://gw.api.tbsandbox.com/router/rest', form_data)
 
rsp = urlopen.read()
rsp = rsp.decode('UTF-8')
print rsp

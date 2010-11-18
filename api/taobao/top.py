#!/usr/bin/env python
# encoding:utf-8
#-------------------------------------------------------------------------------
# Name:        Syndication feed class for subsribtion
# Purpose:
#
# Author:      kokko won
#
# Created:     2010-4-14
# Copyright:   (c) kokkowon.com 2010
#-------------------------------------------------------------------------------

import urllib
import urllib2
import string
import time
import hashlib
import re
import types
import logging
from xml.dom import minidom
#import simplejson

# 淘宝API基类
class TaoBaoAPI(object):
	def __init__ (self):
		self.localTime = time.localtime()
		self.sercetCode = 'test'
		self.appKey = 'test'	
		self.taobaoUrl = 'http://gw.api.taobao.com/router/rest'
		
		self.param = {
			'format':'xml',
			'v':'2.0',
			'method':'',
			'timestamp':time.strftime('%Y-%m-%d %X', self.localTime)
		}
	
	# 设置param参数
	# 
	# @param string field
	# @param mix value
	def setParam (self,field,value):
		self.param[field] = value

	# 获取param参数
	#
	# @param string field
	# @return mix
	def getParam (self,field):
		try:
			value = self.param[field].encode('utf8')
		except KeyError:
			value = None
		return value
	
	# 设置format
	#
	# @param string format
	def setFormat (self,format):
		if format in ('json','xml'):self.setParam('format',format)
	
	# 设置防范
	#
	# @param string method
	def setMethod (self,method):
		#method = 'taobao.'+method
		self.setParam('method',method)
	
	# 签名函数
	#
	# @return sting
	def sign (self):
		src = self.sercetCode + ''.join(["%s%s" % (k, v.encode('utf8')) for k, v in sorted(self.param.items())])
		self.setParam( 'sign',hashlib.md5(src).hexdigest().upper() )
	
	def request (self):
		formData = urllib.urlencode(self.param)
		urlopen = urllib2.urlopen(self.taobaoUrl, formData)
		rsp = urlopen.read()
		rsp = rsp.decode('UTF-8');
		return rsp

# 淘宝客API，扩展Base基类
class TaoBaoKe(TaoBaoAPI):
	# 查询淘宝客推广商品
	def getItems (self):
		self.setMethod('taobao.taobaoke.items.get')
		self.setParam('fields','iid,title,nick,pic_url,price,click_url')
		self.setParam('pid','mm_5410_0_0')
		self.setParam('cid','1512')
		return self.request()
	
	# 查询淘宝客推广商品详细信息
	def getDetail (self):
		self.setMethod('taobao.taobaoke.items.detail.get')
		# ... 相关参数设置
		return None

		
# 测试
# 实例化淘客API
taobaoke = TaoBaoKe()
print taobaoke.getItems()

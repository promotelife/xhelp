#-*- coding:utf-8 -*-	

import xml.etree.ElementTree as ET
import httplib 


class wxChat():
	def __init__(self,data): 
		self.msg_in=self.praseMsg(data)
	def __del__(self):
		pass
		 
	def onSubscribe(self):
		pass 
	def onUnsubscribe(self):
		pass 
	def onText(self):
		pass 
	def onImage(self):
		pass 
	def onLocation(self):
		pass 
	def onLink(self):
		pass 
	def onUnknown(self):
		pass 

	def run(self): 

		#判断事件类型
		msgtype=self.msg_in["MsgType"]
		if msgtype=="event":
			event=self.msg_in["Event"]
			if event=="subscribe": return onSubscribe()
			elif  event=="unsubscribe": return onUnsubscribe()
		elif msgtype=="text": return onText()
		elif msgtype=="image": return onImage()
		elif msgtype=="location": return onLocation()
		elif msgtype=="link": return onLink()
		else : return onUnknown()

	def praseMsg(self,postdata):
		root = ET.fromstring(postdata)
		msg = {}
		for child in root:
			msg[child.tag] = child.text
		return msg	

	def responseText(self,Content): 
		textTpl = """<xml> 
					<ToUserName><![CDATA[%s]]></ToUserName>
					<FromUserName><![CDATA[%s]]></FromUserName>
					<CreateTime>%s</CreateTime>
					<MsgType><![CDATA[%s]]></MsgType>
					<Content><![CDATA[%s]]></Content>
					<FuncFlag>0</FuncFlag>
					</xml>"""
		echostr = textTpl % (self.msg_in['FromUserName']
							,self.msg_in['ToUserName']
							,self.msg_in['CreateTime']
							,"text"
							,Content)			
		return echostr
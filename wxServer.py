#-*- coding:utf-8 -*-
from wxChat import wxChat
from wxStock import getStkmkt
from wxBus import getArrive
from model import Option
searchRange=('stock','bus')
class wxServer(wxChat):
	def __init__(self,data):
		wxChat.__init__(self,data) 
	def onSubscribe(self):
		return self.responseText("欢迎来到！\r小印为您接风了![愉快]\r输入\rset stock 查询股票\rset bus 查询公交到站情况")
	def onUnsubscribe(self):
		return self.responseText("拜拜！\r小印为恭候再次光临")
	def onText(self):
		content=self.msg_in["Content"]
		user=self.msg_in["FromUserName"]
		Option.log(content,user)
		cmds=" ".join(content.lower().strip().split()).split(" ")
		if cmds[0]=="set" :
			if len(cmds)==2 and cmds[1] in searchRange:
				Option.set(user,cmds[1])
				if cmds[1]=="stock":
					return self.responseText("输入代码或者简称可以查行情了哦，\r后面跟上(.hk/sh/sz)还可区分不同市场的股票！") 
				if cmds[1]=="bus":
					return self.responseText("输入公交线路 可以查询公交到站情况了，例如输入：M203") 
			else:
				return self.responseText("请输入set stock 或者 set bus 进行查询设置 ") 
		else:
			cmd=Option.get(user)
			if cmd == "":
				return self.responseText("还没进行查询设置哦，\r 请输入set stock 或者 set bus 进行查询设置 ") 
			elif cmd =="stock":
				return self.responseText(getStkmkt(content)) 
			elif cmd =="bus":
				return self.responseText(getArrive(content)) 
	def onImage(self):
		pass 
	def onLocation(self):
		pass 
	def onLink(self):
		pass 
	def onUnknown(self):
		pass 

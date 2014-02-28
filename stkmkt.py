#-*- coding:utf-8 -*-
import httplib

def getStkmkt(code):
	result=[]
	mkttype=None
	stktype=('gp','gp-b','gp-a')
	mktrange=('hk','sz','sh')
	tmp=code.lower().split('.') 

	tmp[0]=tmp[0].strip()
	if len(tmp)>1 and  tmp[1].strip() in mktrange:
		mkttype= tmp[1].strip()

	codet=getCode(tmp[0])
	if codet is not None:
		codelist=codet.split('^')
		for item in codelist:
			itemt=item.lower().split('~')
			mkt=itemt[0] 
			#print item[4]+stktype[mkttype]
			#print itemt[2].decode('utf-8').encode('GB2312')
			#text = eval("u'"+itemt[2]+"'") 
			#print text.encode('GB2312')
			if (('0000000'+tmp[0]).find(itemt[1])>=0 or tmp[0]==itemt[3]) and mkt in mktrange and itemt[4] in stktype:
				if (mkttype is None or  mkttype==mkt):
					resultt=eval('getStkmkt'+mkt.upper())(itemt[1])
					if(resultt is not None):
						result.append(resultt)
 	if result is None or len(result)==0:
 		result.append('小印暂时还未能理解该代码:'+code)
	return '\r'.join(result)
def getCode(code):
	tmp=None
	try:
		httpc = httplib.HTTPConnection('smartbox.gtimg.cn')
		httpc.request('GET', '/s3/?q='+code+'&t=all',''
			,{'user-agent':'Mozilla/5.0 (Windows NT 5.2; rv:20.0) Gecko/20100101 Firefox/20.0'})
		httpret = httpc.getresponse()
		tmp=httpret.read()
		tmp=tmp.split("=")[1].replace('"','').replace(';','')
		if tmp=='N':
			tmp=None
	except:
		tmp=None
	return tmp

def getStkmktHK(code):
	tmp=None
	try:
		httpc = httplib.HTTPConnection('qt.gtimg.cn')
		httpc.request('GET', '/q=hk'+code,'',{'user-agent':'Mozilla/5.0 (Windows NT 5.2; rv:20.0) Gecko/20100101 Firefox/20.0'})
		httpret = httpc.getresponse()
		tmp=httpret.read()
	except:
		tmp=""
	if(tmp.find(code)<0):
		return None
	tmp=tmp.split("=")[1].replace('"','').split('~')
	#for i in range(len(tmp)): 
	#	print str(i)+'	'+tmp[i]
	result="%s(%s)：现价%s，上涨%s，涨幅%s%%，最高%s，最低%s，成交量%s股，成交额%s，成交价%s"
	result=result+"，开盘价%s，昨收价%s，振幅%s%%，52周最高%s，52周最低%s，市盈率%s，总市值%s【更新时间%s】"
	result=result %(tmp[1].decode('GB2312').encode('utf8'),tmp[2],tmp[35],tmp[31],tmp[32],tmp[33],tmp[34],tmp[36],tmp[37],tmp[9]
		,tmp[5],tmp[4],tmp[43],tmp[48],tmp[49],tmp[39],tmp[44],tmp[30])
	result=result+'\r<a href="http://gp.3g.qq.com/g/stock/wap3/index.html'
	result=result+'?sid=ASZeItvwAlJNIRSIZo1YTt8K&icfa=stockhk_h#page=StockHK&securitiesId=share_'+code+'.xhkg"'
	result=result+'>点击我查看详情</a>'
	return result

def getStkmktSZ(code):  
	tmp=None
	try:
		httpc = httplib.HTTPConnection('qt.gtimg.cn')
		httpc.request('GET', '/q=sz'+code,'',{'user-agent':'Mozilla/5.0 (Windows NT 5.2; rv:20.0) Gecko/20100101 Firefox/20.0'})
		httpret = httpc.getresponse()
		tmp=httpret.read() 
	except:
		tmp=""
	if(tmp is not None and tmp.find(code)<0):
		return None
	tmp=tmp.split("=")[1].replace('"','').split('~')
	#for i in range(len(tmp)): 
	#	print str(i)+'	'+tmp[i]
	result="%s(%s)：现价%s，上涨%s，涨幅%s%%，最高%s，最低%s，成交量%s股，成交额%s，成交价%s"
	result=result+"，开盘价%s，昨收价%s，振幅%s%%，52周最高%s，52周最低%s，市盈率%s，总市值%s【更新时间%s】"
	result=result %(tmp[1].decode('GB2312').encode('utf8'),tmp[2],tmp[35],tmp[31],tmp[32],tmp[33],tmp[34],tmp[36],tmp[37],tmp[9]
		,tmp[5],tmp[4],tmp[43],tmp[48],tmp[49],tmp[39],tmp[44],tmp[30])
	result=result+'\r<a href="http://gp.3g.qq.com/g/stock/wap3/index.html#page=Stock&securitiesId=share_'+code+'.xshe"'
	result=result+'>点击我查看详情</a>'
	return result

def getStkmktSH(code):
	tmp=None
	try:
		httpc = httplib.HTTPConnection('qt.gtimg.cn')
		httpc.request('GET', '/q=sh'+code,'',{'user-agent':'Mozilla/5.0 (Windows NT 5.2; rv:20.0) Gecko/20100101 Firefox/20.0'})
		httpret = httpc.getresponse()
		tmp=httpret.read() 
	except:
		tmp=""
	if(tmp is not None and tmp.find(code)<0):
		return None
	tmp=tmp.split("=")[1].replace('"','').split('~')
	#for i in range(len(tmp)): 
	#	print str(i)+'	'+tmp[i]
	result="%s(%s)：现价%s，上涨%s，涨幅%s%%，最高%s，最低%s，成交量%s股，成交额%s，成交价%s"
	result=result+"，开盘价%s，昨收价%s，振幅%s%%，52周最高%s，52周最低%s，市盈率%s，总市值%s【更新时间%s】"
	result=result %(tmp[1].decode('GB2312').encode('utf8'),tmp[2],tmp[35],tmp[31],tmp[32],tmp[33],tmp[34],tmp[36],tmp[37],tmp[9]
		,tmp[5],tmp[4],tmp[43],tmp[48],tmp[49],tmp[39],tmp[44],tmp[30])
	result=result+'\r<a href="http://gp.3g.qq.com/g/stock/wap3/index.html#page=Stock&securitiesId=share_'+code+'.xshg"'
	result=result+'>点击我查看详情</a>'
	return result

#判断字符窜是否是数字
def checkNum(code):
	try:
		x=int(code)
	except ValueError:
		return False
	return True
if __name__ == '__main__':  
	print getStkmkt('300333')
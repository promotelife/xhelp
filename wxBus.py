#-*- coding:utf-8 -*-
import httplib
import json
import re

def getArrive(code):
	eid=getEid(code)
	if eid is None: return "未能查到"+code+'"的信息'
	sids=getSid(code)
	tmp=getURL("busi.gpsoo.net",'/v1/bus/get_online_gps?school_id='+eid) 

  
	#替换掉以0开头的数字为字符窜
	ll= re.findall(r",(0\d),",tmp) 
	if len(ll)>0 : tmp=tmp.replace(','+ll[0]+',',',"'+ll[0]+'",')

	car_info = json.loads(tmp)
	cur_station=int(car_info["key"]["cur_station"])
	next_station=int(car_info["key"]["next_station"])
	user_name=int(car_info["key"]["user_name"] )
	cur_station_state=int(car_info["key"]["cur_station_state"] )
	subline_id=int(car_info["key"]["subline_id"] )
 	route='即将到站：'
	for x in sids:
		sid=x["id"] 
		route=route+"\r往"+x["end_station"].encode('utf8')+"方向：\r"
		for a in car_info["records"]: 
			if a[next_station].encode('utf8')!="" and sid==a[subline_id]:
				route=route+','+a[next_station].encode('utf8')
	return route
def getSubline(sid):
	#http://busi.gpsoo.net/v1/bus/get_subline_inf?mapType=G_NORMAL_MAP&sid=79389
	tmp=getURL("busi.gpsoo.net",'/v1/bus/get_subline_inf?mapType=G_NORMAL_MAP&sid='+sid) 
	sidinfo= json.loads(tmp) 
	return sidinfo["data"]["stations"]  

def getSid(linename): 
	#http://busi.gpsoo.net/v1/bus/get_lines_by_city?type=handset&city_id=860515&line_name=383 
	tmp=getURL("busi.gpsoo.net",'/v1/bus/get_lines_by_city?type=handset&city_id=860515&line_name='+linename) 
	#{"data":[
	#{"begin_time":"06:00","dir":"0","end_station":"科技园公交站","end_time":"23:00","id":"79389","isopen":"1","line_name":"383","price":"6","start_station":"南湾樟树布村总站"}
	#,{"begin_time":"06:15","dir":"1","end_station":"南湾樟树布村总站","end_time":"23:00","id":"79432","isopen":"1","line_name":"383","price":"6","start_station":"科技园公交站"}
	#],"msg":"ok","success":"true"}
	sinfo= json.loads(tmp) 
	return sinfo["data"]  
def getEid(linename):
	tmp=getURL("busi.gpsoo.net",'/v1/bus/t_lineisopen?code=860515&line='+linename)
	#{"success":"true","msg":"ok","data":[{"eid":"1554077","isopen":"1"}]}
	try: 
		eidinfo= json.loads(tmp)  
		return  eidinfo["data"][0]["eid"]
	except:
		return None


def getURL(domain,params):
	try:
		httpc = httplib.HTTPConnection(domain)
		httpc.request('GET',params,''
			,{'user-agent':'Mozilla/5.0 (Windows NT 5.2; rv:20.0) Gecko/20100101 Firefox/20.0'})
		httpret = httpc.getresponse()
		tmp=httpret.read()
		#tmp=tmp.split("=")[1].replace('"','').replace(';','')
		if tmp=='N':
			tmp=None
	except:
		tmp=None
	return tmp

#860515 深圳代码 
if __name__ == '__main__':   
	print getArrive('303')   
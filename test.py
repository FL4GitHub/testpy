# encoding: UTF-8

import sys
import base64
import hashlib
import urllib
import urllib2
import hashlib
import re
import requests
import time
import threading
#Timer（定时器）是Thread的派生类，
#用于在指定时间后调用一个方法。

Cookie = "cna=oFvVEIX+DhICAXJQ6702ODAV; juid=01b3p5oeme1n7d; __ali=1481534882799BFE; __aliCount=1; __ysuid=14815949518012fL; advideo88186_1=2; advideo88186_2=1; __aryft=1481687694; logCookieKey=invalid; __utmarea=; ykss=9d1c5158333967346cd3840d; P_j_scl=hasCheckLogin; _l_lgi=368889439; yseid=1481788888893hJGAaI; yseidcount=5; u=ibaige; rpvid=1481792368576RDF-1481792553888; ypvid=14817976509134lJxd9; ysestep=25; yseidtimeout=1481804850914; ycid=0; ystep=62; seid=01b410bif62fdo; referhost=http%3A%2F%2Fv.youku.com; seidtimeout=1481799450919; __ayft=1481594951776; __aysid=1481534878531kwx; __arpvid=14817976509677Lr95s-1481797650979; __arycid=dd-3-2038; __ayscnt=1; __arcms=dd-3-2038; __aypstp=72; __ayspstp=77; yktk=1%7C1481797652%7C15%7CaWQ6MzY4ODg5NDM5LG5uOmliYWlnZSx2aXA6ZmFsc2UseXRpZDozNjg4ODk0MzksdGlkOjA%3D%7C54e8cd8d74d0e19b64579488fb42db57%7C3ec86237d7f2a51cba69c3ac62c448eca899767e%7C1; szutsid=368889439; __ayvstp=242; __aysvstp=248; cod=73; sdmenu_my_menu=11111100100; JSESSIONID=9340C24CC89B56A4C51ADB2AE5D75CEE; last_aid=a119; last_url=manager-special-check.do; refresh_btn_left=1541px; refresh_btn_top=405px"
special_url = 'http://10.25.12.58:8090/manager-special-check.do?specialQuery.itemurl=&specialQuery.iid=&specialQuery.uid=&specialQuery.aid=&specialQuery.type=&specialQuery.orderFlag=0&type=1'
auto_url = 'http://10.25.12.58:8090/manager-auto-check.do?autoQuery.itemurl=&autoQuery.iid=&autoQuery.uid=&autoQuery.aid=&autoQuery.type=&autoQuery.orderFlag=0&type=1'
old_url = 'http://10.25.12.58:8090/manager-old-check.do?oldQuery.itemurl=&oldQuery.iid=&oldQuery.uid=&oldQuery.aid=&oldQuery.type=&oldQuery.orderFlag=0&type=1'
check_url = 'http://10.25.12.58:8090/manager-censor-list.do?commentQuery.itemurl=&commentQuery.iid=&commentQuery.uid=&commentQuery.aid=&commentQuery.type=1&commentQuery.status=2&commentQuery.orderFlag=0&type=1'
special_check_url = 'http://10.25.12.58:8090/manager-batch-update-special.do'
special_data = 'specialQuery.itemurl=&specialQuery.iid=&specialQuery.uid=&specialQuery.aid=&specialQuery.type=&specialQuery.orderFlag=0&op=-2'
auto_check_url = 'http://10.25.12.58:8090/manager-batch-update-auto.do'
auto_data = 'autoQuery.itemurl=&autoQuery.iid=&autoQuery.uid=&autoQuery.aid=&autoQuery.type=&autoQuery.orderFlag=0&op=-2'
old_check_url='http://10.25.12.58:8090/manager-batch-update-old.do?'
old_data = 'oldQuery.itemurl=&oldQuery.iid=&oldQuery.uid=&oldQuery.aid=&oldQuery.type=&oldQuery.orderFlag=0&op=-2'
# autoQuery.itemurl=&autoQuery.iid=&autoQuery.uid=&autoQuery.aid=&autoQuery.type=&autoQuery.orderFlag=0&op=-2

def get_check_id(html):
    ids = re.findall('name="id" value="(.*?)"',html,re.I)
    return ids
def get_task(url):
	headers = {
				'Cookie': Cookie
				}
	data = None
	req = urllib2.Request(url, data, headers)
	response = urllib2.urlopen(req)
	html = response.read()
	return html
def auto_check(ids,url,data):
	for i in range(len(ids)):
		notchooseid = ids[i]
		delreason = 'delreason_'+notchooseid
		data = data + "&notchooseid="+notchooseid+"&"+delreason +"=0"
	headers = {
				'Host': '10.25.12.58:8090',
				'Cache-Control': 'max-age=0',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'Cookie': Cookie,
				'Origin': 'http://10.25.12.58:8090',
				'Upgrade-Insecure-Requests': '1',
				'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
				'Accept-Encoding': 'gzip, deflate',
				'Accept-Language': 'zh-CN,zh;q=0.8',
				'Content-Type': 'application/x-www-form-urlencoded'
				}
	requests.post(url,data=data,headers=headers)
def task():  
	auto_check(get_check_id(get_task(special_url)),special_check_url,special_data)
	auto_check(get_check_id(get_task(auto_url)),auto_check_url,auto_data)
	auto_check(get_check_id(get_task(old_url)),old_check_url,old_data)
	print "task ..."  

i = 0
while (i<10000):
	i=i+1
	task()
	#time.sleep(0.1)

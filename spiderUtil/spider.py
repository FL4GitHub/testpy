# -*- coding: UTF-8 -*-
import sys
import base64
import hashlib
import urllib
import urllib2
import hashlib
import re
import requests
import time
import json
import csv
import codecs
import hashlib

def md5(s):
    m2 = hashlib.md5()
    m2.update(s)
    return m2.hexdigest()

def get_task(url):
    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
    return html
def get_sign(ct,createtime,uid,iid,content):
    sign = ""
    if (ct == "1001"):
        secretkey = "Ef9/4e4d^@g9a2M3g"
    elif(ct == "2001"):
        secretkey = "w$7s0%9dg2j+02B76ds*6Lv"
    elif(ct == "2002"):
        secretkey = "GtAWjdKv9uc&0bRcbV5Y2!"
    elif(ct == "2003"):
        secretkey = "wh6i_#+T_50a3X&ceE_7;Yp"
    elif(ct == "3001"):
        secretkey = "Ofeid9M*2Rf8@v3o;dkcf"
    elif(ct == "3002"):
        secretkey = "W;a!tV3o/cu53WhMjoG2FY"
    elif(ct == "4001"):
        secretkey = "BsjeX4g0y8vpi3d2J3=q3L"
    elif(ct == "4002"):
        secretkey = "jggA%#JSrwTt$@E#Z0kfB8"
    elif(ct == "5001"):
        secretkey = "!@*k2f$Gc%35!O24&REOfK"
    else:
        secretkey = "Ef9/4e4d^@g9a2M3g"

    sign = secretkey+str(createtime)[:-3]+str(uid)+str(iid)+str(content)
    print sign
    sign = md5(sign)

    return sign

def compare_list(iid,type):
    if type == 1:
        host = "106.11.187.52"
        file = str(iid)+"Aone.txt"
    else:
        host = "service.danmu.youku.com"
        file = str(iid)+"M6.txt"
    print(file)
    fout = open(file, "w")
    n = 1
    m = 0
    while m<100:
        url = "http://"+host+"/list?iid=472398842&mcount=1&ct=3001&mat="+str(m)
        m = m+1
        r = get_task(url)
        json_r = json.loads(r)
        #print json_r
        for i in json_r["result"]:
            # if (n==1):
            #     spamwriter.writerow(["index","id","iid","uid","mat","playat","ver","propertis","content","createtime","status","ipaddr","lid","ouid","aid","type","level","ct","sign"])
            n = n+1
            #print len(i)
            id = str(i["id"])
            iid = str(i["iid"])
            uid = "2016122101"
            mat = str(i["mat"])
            playat = str(i["playat"])
            ver = str(i["ver"])
            propertis = str(i["propertis"])
            content = i["content"]
            createtime = (i["createtime"])
            status = i["status"]
            ipaddr = i["ipaddr"]
            lid = str(i["lid"])
            ouid = str(i["ouid"])
            aid = str(i["aid"])
            type = str(i["type"])
            level = str(i["level"])
            ct = str(i["ct"])
            content = content.encode("utf-8")

            # if (ct == 0):
            #     ct = 3001
            # sign = get_sign(ct,createtime,uid,iid,content)
            str_a=''
            mylist=[]
            for k,v in i.items():
                mylist.append(k)
            mylist.sort()

            myret=[]
            for k in mylist:
                # if k == "iid":
                #     i[k] = "382187529"
                # if k == "uid":
                #     i[k] = "2016122101"
                # if k == "createtime":
                #     i[k] = str(i[k])[:-3]
                if k == "propertis":
                    i[k] = i[k].replace(' ','').replace('\r','').replace('\n','')
                if k == "content":
                    i[k] = i[k].encode("utf-8")
                myret.append(str(i[k]))
            myret.insert(0,str(n))
            # myret.append(sign)
            str_b = "\t".join(myret) +"\n"
            #print str_b
            #print ",".join(mylist)
            #print myret
            #line = str(n)+"\t"+id+"\t"+iid+"\t"+uid+"\t"+mat+"\t"+playat+"\t"+ver+"\t"+propertis+"\t"+content+"\t"+createtime+"\t"+status+"\t"+ipaddr+"\t"+lid+"\t"+ouid+"\t"+aid+"\t"+type+"\t"+level+"\t"+ct+"\t"+sign+"\r\n"
            fout.write(str_b)
            #spamwriter.writerow([n,id,iid,uid,mat,playat,ver,propertis,content,createtime,status,ipaddr,lid,ouid,aid,type,level,ct,sign])
    fout.close()






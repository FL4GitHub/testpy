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


#youku_home_url = "http://www.youku.com/"


def get_vids_by_youku_home(url="http://www.youku.com"):
    vids = []
    vcodes = get_vcodes_by_youku_home(url)
    vids = vcodes_2_vids(vcodes)
    return vids

def get_vcodes_by_youku_home(url="http://www.youku.com"):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'
    }
    page = requests.get(url,headers=headers)
    text = page.text
    ids = re.findall('<a href="http://v.youku.com/v_show/id_(.*?).html',text)
    print(len(ids))
    return ids
def vcodes_2_vids(vcodes):
    vids = [vcode_2_vid(vcode) for vcode in vcodes]
    return vids

def vcode_2_vid(vcode):
    try:
        vcode = vcode[1:]
        vcode = base64.b64decode(vcode)
        vcode = int(vcode) >> 2
        vid = vcode
        #print(vcode)
    except:
        print("err*****"+vcode)
    return vid

def check_is_danmu_vid(host,vid):
    url = "http://"+host+"/profile?ct=3001&iid="+str(vid)
    res = requests.get(url)
    return res.text

def check_is_danmu_vids(vids):
    danmu_vids = []
    not_danmu_vids = []
    for vid in vids:
        profile_res = check_is_danmu_vid(vid)
        profile_res = json.loads(profile_res)
        #profile_res = eval(profile_res)
        m_points = profile_res['m_points']
        if m_points == "0":
            not_danmu_vids.append(vid)
        else:
            danmu_vids.append(vid)
    print("danmu_vids.append",len(danmu_vids))
    print("not_danmu_vids.append",len(not_danmu_vids))
    return danmu_vids

def get_vids_by_aid(url):
    vids = []
    return vids



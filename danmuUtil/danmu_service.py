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
from spiderUtil.spider import *




def get_profile(host,iid):
    url = "http://"+host+"/profile?ct=3001&iid="+str(iid)
    res = requests.get(url)

    return json.loads(res.text)


def get_list(host,iid,mat):
    url = "http://"+host+"/list?ct=3001&mcount=1&iid="+str(iid)+"&mat="+mat
    res = requests.get(url)
    return res.text

def compare_list_by_iid(iid):
    Aone_list =  compare_list(iid,1)
    M6_list = compare_list(iid,2)



def compare_list_mat(iid,type,mat):
    if type == 1:
        host = "106.11.187.52"
    else:
        host = "service.danmu.youku.com"
    return get_list(host,iid,mat)
# -*- coding: UTF-8 -*-

import sys
from spiderUtil.getvid import *
from danmuUtil.danmu_service import *

M6_host = "service.danmu.youku.com"
Aone_host = "106.11.187.52"
vids = get_vids_by_youku_home("http://www.youku.com/?spm=a2hzp.8253869.qheader.5~5~5!3~1~3~A")

correct_vids = []
incorrect_vids = []

def compare_mpoints(vids):
    i=0
    for vid in vids:
        i=i+1
        print(i)
        M6_profile = get_profile(M6_host,vid)
        Aone_profile = get_profile(Aone_host,vid)
        M6_mponits = M6_profile['m_points']
        Aone_mponits = Aone_profile['m_points']
        if M6_mponits == Aone_mponits:
            correct_vids.append(vid)
        else:
            incorrect_vids.append(vid)
            print("*******M6",M6_profile)
            print("*******Aone",Aone_profile)




compare_mpoints(vids)
print(u"不正确的数量",len(incorrect_vids))
print(u"正确的数量",len(correct_vids))


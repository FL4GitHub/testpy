# -*- coding: UTF-8 -*-

import sys
from spiderUtil.getvid import *
from danmuUtil.danmu_service import *
from spiderUtil.spider import *






def compare_list_by_iid_mat(iid,mat):
    Aone_list =  compare_list_mat(iid,1,mat)
    M6_list = compare_list_mat(iid,2,mat)
    if M6_list!= Aone_list:
        print("******Aone",Aone_list)
        print("******M6",M6_list)
        print("fail",iid,mat)
    else:
        print("******Aone",Aone_list)
        print("******M6",M6_list)
        print("success",iid,mat)


compare_list_by_iid_mat("382849475","3")




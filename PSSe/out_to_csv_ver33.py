# -*- coding: utf-8 -*-
def out_to_csv(file_name):
    # Dynamic 시뮬레이션 수행 후 얻은 out파일을 불러들이고 이를 csv파일 형태로 저장
    chnfobj = dyntools.CHNF(file_name + ".out")
    short_tilte, chanid, chandata = chnfobj.get_data()

    A = list(chanid.items())

    C = []

    for i in range(len(A)):
        B = [A[i][1]]
        B += chandata[A[i][0]]
        C.append(B)

    df = pd.DataFrame(C)
    df = df.transpose()
    df.to_csv(file_name + ".csv", header=None, index=None)

    return C

# -*- coding: utf-8 -*-
import os
import sys

sys.path.append(os.getcwd() + str(r"""\file"""))
PSSE33_PATH = r"""C:\Program Files (x86)\PTI\PSSE33\PSSBIN"""
sys.path.append(PSSE33_PATH)
os.environ['PATH'] += ';' + PSSE33_PATH

import psspy
import redirect
import dyntools
import re

import pandas as pd
# import numpy as np

# PSS/e 변수 사용할 수 있도록 선언
_i = psspy.getdefaultint()
_f = psspy.getdefaultreal()
_s = psspy.getdefaultchar()

reload(sys)
sys.setdefaultencoding('cp949')

# PSS/E 실행
psspy.psseinit(50000)
redirect.psse2py()
####################################### 해당 부분까지는 Default로 적용하면 될 것 같다. #######################################

reload(sys)
sys.setdefaultencoding('cp949')

out_to_csv("Test5")

print("Finished")
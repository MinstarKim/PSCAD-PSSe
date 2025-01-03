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

import os
import sys
import pandas as pd

# PSS/E 경로를 가지고 오는 부분
sys.path.append(r"C:\Program Files\PTI\PSSE35\35.2\PSSBIN")
os.environ['PATH'] = (r"C:\Program Files\PTI\PSSE35\35.2\PSSBIN;" + os.environ['PATH'])
sys.path.append(r"C:\Program Files\PTI\PSSE35\35.2\PSSPY37")
os.environ['PATH'] = (r"C:\Program Files\PTI\PSSE35\35.2\PSSPY37;" + os.environ['PATH'])

# 전처리기
import psse35
import psspy
psspy.throwPsseExceptions = True
import redirect
import dyntools
import re

# PSS/E 실행
psspy.psseinit(50000)
redirect.psse2py()
####################################### 해당 부분까지는 Default로 적용하면 될 것 같다. #######################################

out_to_csv("test_statcom")

print("Finished")
# -*- coding: utf-8 -*-
# 다만 이 경우 pandas를 필요
# 경고: 해당 csv가 이전 clipboard_to_csv 코드를 기반으로 생성했다고 간주하기 때문에 개별 csv 의 time에 대한 정보가 지워지는 결과 발생
# Domain만 지우고 합침

import pandas as pd

################################################ Directory +  File name ################################################

path = r"""C:\Fast_EMT_final\UVRT_5"""
name_list = [r"""\PSCAD_result1.csv""", r"""\PSCAD_result1.csv"""]
result_name = r"""\Result.csv"""

########################################################################################################################

A = pd.read_csv(path + name_list[0])

for i in range(len(name_list)-1):
    B = pd.read_csv(path + name_list[i+1])
    B = B.drop('Domain', axis=1)
    A = pd.concat([A, B], axis=1)

A.to_csv(path + result_name, index = False)




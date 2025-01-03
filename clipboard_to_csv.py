# -*- coding: utf-8 -*-
import sys
import clipboard

# Load data from clipboard and save as csv file
data = clipboard.paste()

################################################ Directory +  File name ################################################

path = r"""C:/Users/CH/Downloads/"""
name = r"""Result_test.csv"""

########################################################################################################################

sys.stdout = open(path+name, 'w')
print(data)
sys.stdout.close()
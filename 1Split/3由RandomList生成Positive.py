from numpy import *
import numpy as np
import random
import math
import os
import time
import pandas as pd
import csv
import math
import random

# 定义函数
def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:  # 把每个rna疾病对加入OriginalData，注意表头
        SaveList.append(row)
    return

def ReadMyCsv2(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:
        counter = 0
        while counter < len(row):
            row[counter] = int(row[counter])      # 转换数据类型
            counter = counter + 1
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return

NewRandomList = []
ReadMyCsv2(NewRandomList, 'NewRandomList.csv')

NewAllEdgeNum = []
ReadMyCsv(NewAllEdgeNum, 'DrugandProtien.csv')

PositiveSample = []
counter = 0
while counter < len(NewRandomList):
    counter1 = 0
    while counter1 < len(NewRandomList[counter]):
        PositiveSample.append(NewAllEdgeNum[NewRandomList[counter][counter1]])
        counter1 = counter1 + 1
    print(counter)
    counter = counter + 1



StorFile(PositiveSample, 'PositiveSample.csv')

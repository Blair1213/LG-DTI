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
import copy

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

AllNode = []
ReadMyCsv(AllNode, 'AllNode.csv')

FinalProteinFeatureNum = []
ReadMyCsv(FinalProteinFeatureNum, 'FinalProteinNum.csv')

FinalDiseaseFeatureNum = []
ReadMyCsv(FinalDiseaseFeatureNum, 'FinalDrugNum.csv')

# 生成AllNodeManner
counterP = 0
while counterP < 5:
    LineEmbeddingName = 'vec_all' + str(counterP) + '.txt'
    LineEmbedding = np.loadtxt(LineEmbeddingName, dtype=str, skiprows=1)
    LineEmbedding = np.loadtxt(LineEmbeddingName, dtype=str, skiprows=1)


    # manner
    AllNodeMannerNum = []
    counter = 0
    while counter < len(AllNode):
        pair = []
        counter1 = 0
        while counter1 < len(LineEmbedding[0]) - 1:        # 如果节点孤立，则Feature全为0
            pair.append(0)
            counter1 = counter1 + 1
        AllNodeMannerNum.append(pair)
        counter = counter + 1

    # manner
    counter = 0
    while counter < len(LineEmbedding):
        num = int(LineEmbedding[counter][0])
        AllNodeMannerNum[num] = list(LineEmbedding[counter][1:])
        counter = counter + 1

    print(np.array(AllNodeMannerNum).shape)
    AllNodeMannerNumName = 'AllNodeMannerNum' + str(counterP) + '.csv'
    StorFile(AllNodeMannerNum, AllNodeMannerNumName)


    num1 = 0
    # 将lnc和disease的feature加入manner中，[manner,lnc/disease]
    counter = 0
    while counter < len(FinalDiseaseFeatureNum):
        AllNodeMannerNum[int(FinalDiseaseFeatureNum[counter][0])].extend(FinalDiseaseFeatureNum[counter][1:])
        num1 = num1 + 1
        counter = counter + 1
    print(num1)

    num2 = 0
    counter = 0
    while counter < len(FinalProteinFeatureNum):
        AllNodeMannerNum[int(FinalProteinFeatureNum[counter][0])].extend(FinalProteinFeatureNum[counter][1:])
        num2 = num2 + 1
        counter = counter + 1
    print(num2)

    print(np.array(AllNodeMannerNum).shape)
    AllNodeFeatureNumName = 'AllNodeAttributeMannerNum' + str(counterP) + '.csv'
    StorFile(AllNodeMannerNum, AllNodeFeatureNumName)

    counterP = counterP + 1



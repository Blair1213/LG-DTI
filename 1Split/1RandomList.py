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

def partition(ls, size):
    """
    Returns a new list with elements
    of which is a list of certain size.

        >>> partition([1, 2, 3, 4], 3)
        [[1, 2, 3], [4]]
    """
    return [ls[i:i+size] for i in range(0, len(ls), size)]


# 形成一个随机列表打乱数据集，并保存
# 数据
NewAllEdgeNum = []
ReadMyCsv(NewAllEdgeNum, "DPDrugBankDrugProtein5.csv")
print('NewAllEdgeNum[0]', NewAllEdgeNum[0])
print(len(NewAllEdgeNum))



# 由AllEdge产生RandomList
RandomList = random.sample(range(0, len(NewAllEdgeNum)), len(NewAllEdgeNum))
print('len(RandomList)', len(RandomList))
NewRandomList = partition(RandomList, math.ceil(len(RandomList) / 5))
print('len(NewRandomList[0])', len(NewRandomList[0]))
StorFile(NewRandomList, 'NewRandomList.csv')


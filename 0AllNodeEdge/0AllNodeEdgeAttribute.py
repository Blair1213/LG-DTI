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

def ReadMyCsv(SaveList, fileName):
    csv_reader = csv.reader(open(fileName))
    for row in csv_reader:          # 注意表头
        SaveList.append(row)
    return

def StorFile(data, fileName):
    with open(fileName, "w", newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    return


# 数据
# LD
LDAllLncDisease = []
ReadMyCsv(LDAllLncDisease, "LDAllLncDisease.csv")
print('LDAllLncDisease[0]', LDAllLncDisease[0])

# LM
LMSNPLncMi = []
ReadMyCsv(LMSNPLncMi, "LMSNPLncMi.csv")
print('LMSNPLncMi[0]', LMSNPLncMi[0])

# LP
LPLncRNA2TargetLncProtein3 = []
ReadMyCsv(LPLncRNA2TargetLncProtein3, "LPLncRNA2TargetLncProtein3.csv")
print('LPLncRNA2TargetLncProtein3[0]', LPLncRNA2TargetLncProtein3[0])

# MD
MDCuiMiDisease = []
ReadMyCsv(MDCuiMiDisease, "MDCuiMiDisease.csv")
print('MDCuiMiDisease[0]', MDCuiMiDisease[0])

# MP
MPmiRTarBaseMiProtein9 = []
ReadMyCsv(MPmiRTarBaseMiProtein9, "MPmiRTarBaseMiProtein5.csv")
print('MPmiRTarBaseMiProtein9[0]', MPmiRTarBaseMiProtein9[0])

# PDisease
PDDisGeNETProteinDisease15 = []
ReadMyCsv(PDDisGeNETProteinDisease15, "PDDisGeNETProteinDisease20.csv")
print('PDDisGeNETProteinDisease15[0]', PDDisGeNETProteinDisease15[0])

# DD
DDDrugDisease = []
ReadMyCsv(DDDrugDisease, "DrugDiseaseDrugDisease.csv")
print('DDDrugDisease[0]', DDDrugDisease[0])

# PDrug
PDDrugBankAllProteinDrug5 = []
ReadMyCsv(PDDrugBankAllProteinDrug5, "DPDrugBankDrugProtein5.csv")
print('PDDrugBankAllProteinDrug5[0]', PDDrugBankAllProteinDrug5[0])

# PPI
PPI = []
ReadMyCsv(PPI, "PPI.csv")
print('PPI[0]', PPI[0])

# AllEdge
AllEdge = []
AllEdge.extend(LDAllLncDisease)
AllEdge.extend(MDCuiMiDisease)
AllEdge.extend(LMSNPLncMi)
AllEdge.extend(MPmiRTarBaseMiProtein9)
AllEdge.extend(LPLncRNA2TargetLncProtein3)
AllEdge.extend(PDDisGeNETProteinDisease15)
#AllEdge.extend(PDDrugBankAllProteinDrug5)
AllEdge.extend(DDDrugDisease)
AllEdge.extend(PPI)
print(len(AllEdge))
print(AllEdge[0])
StorFile(AllEdge, 'AllEdge.csv')


# 节点
FinalDiseaseFeature = []
ReadMyCsv(FinalDiseaseFeature, "FinalDiseaseFeature.csv")
FinalAllDisease = np.array(FinalDiseaseFeature)[:, 0]
print('len(FinalAllDisease)', len(FinalAllDisease))
print('FinalAllDisease[0]', FinalAllDisease[0])

FinalDrugFeature = []
ReadMyCsv(FinalDrugFeature, "FinalDrugFeature.csv")
FinalAllDrug = np.array(FinalDrugFeature)[:, 0]
print('len(FinalAllDrug)', len(FinalAllDrug))
print('FinalAllDrug[0]', FinalAllDrug[0])

FinalLncKmer = []
ReadMyCsv(FinalLncKmer, "FinalLncKmer.csv")
FinalLnc = np.array(FinalLncKmer)[:, 0]
print('len(FinalLnc)', len(FinalLnc))
print('FinalLnc[0]', FinalLnc[0])

FinalMiKmer = []
ReadMyCsv(FinalMiKmer, "FinalMiKmer.csv")
FinalMi = np.array(FinalMiKmer)
FinalMi = FinalMi[:, 0]
print('len(FinalMi)', len(FinalMi))
print('FinalMi[0]', FinalMi[0])

FinalProteinFeature = []
ReadMyCsv(FinalProteinFeature, "FinalProteinFeature.csv")
FinalProtein = np.array(FinalProteinFeature)[:, 0]
print('len(FinalProtein)', len(FinalProtein))
print('FinalProtein[0]', FinalProtein[0])

# AllNode
AllNode = []
AllNode.extend(FinalMi)
AllNode.extend(FinalLnc)
AllNode.extend(FinalProtein)
AllNode.extend(FinalAllDisease)
AllNode.extend(FinalAllDrug)

print('len(AllNode)', len(AllNode))
counter = 0
while counter < len(AllNode):
    pair = []
    pair.append(AllNode[counter])
    AllNode[counter] = pair
    counter = counter + 1
print(AllNode[0])
StorFile(AllNode, 'AllNode.csv')

# AllNode
AllNodeAttribute = []
AllNodeAttribute.extend(FinalMiKmer)
AllNodeAttribute.extend(FinalLncKmer)
AllNodeAttribute.extend(FinalProteinFeature)
AllNodeAttribute.extend(FinalDiseaseFeature)
AllNodeAttribute.extend(FinalDrugFeature)


StorFile(AllNodeAttribute, 'AllNodeAttribute.csv')
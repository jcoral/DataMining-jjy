# -*- coding: utf-8 -*-

import copy
import numpy as np

def calDistance(point, v):
    """
    计算点到一个分类的距离
    :param point: 点
    :param v: 一个分类
    :return:
    """
    vCenterPoint = [0, 0]
    vLength = len(v)
    if vLength == 0: return 0
    for p in [0, 1]:
        axsSum = 0
        for vp in v:
            axsSum += vp[p]
        vCenterPoint[p] = float(axsSum) / float(vLength)
    return np.sqrt(sum([(point[0] - vCenterPoint[0])**2, (point[1] - vCenterPoint[1])**2]))

def classBoxSame(b1, b2):
    """
    判断两个分类是否一样
    """
    if b1 == None or b2 == None: return False
    for bindex in range(len(b1)):
        for pindex in range(len(b1[bindex])):
            if len(b1[bindex]) != len(b2[bindex]): return False

            isSamePoint = b1[bindex][pindex][0] == b2[bindex][pindex][0]
            isSamePoint = isSamePoint and b1[bindex][pindex][1] == b2[bindex][pindex][1]
            if not isSamePoint:
                return False
    return True

def KMeans(dataSet = [[]], k = 2):
    preClassBox = list()
    for i in range(k):
        il = list()
        il.append(dataSet[i])
        preClassBox.append(il)
    while True:
        classBox = list()
        # 初始化classBox
        for i in range(k):
            il = list()
            il.append(dataSet[i])
            classBox.append(list())

        # 遍历每一个点
        for dsIndex in range(len(dataSet)):
            dsItem = dataSet[dsIndex]
            minDistIndex = 0
            minCBDist    = None

            # 计算当前点与分类最小的距离
            for cbIndex in range(len(preClassBox)):
                cbDist = calDistance(dsItem, preClassBox[cbIndex])
                if minCBDist == None or cbDist < minCBDist:
                    minDistIndex = cbIndex
                    minCBDist = cbDist
            classBox[minDistIndex].append(dsItem)

        isSame = classBoxSame(preClassBox, classBox)
        if preClassBox != None and isSame:
            return classBox
        else:
            preClassBox = classBox



if __name__ == "__main__":
    print KMeans(dataSet=[[9, 2], [9, 3], [0, 1], [0, 2]])
















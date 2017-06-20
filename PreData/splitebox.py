# -*- coding: utf-8 -*-

import numpy as np
import copy
def calBoxLength(originData, boxPos, minPos, minValue):
    """
    :param boxPos: [(startPosition, length), ...]
    :param minPos: [(startPostion, length), ...]
    :return:
    """
    box = list()
    for startPosition, length in boxPos:
        box.append(originData[startPosition : startPosition + length])

    sse = 0
    for boxItems in box:
        sse += np.var(boxItems)

    if minPos == None or sse < minValue:
        minValue = sse
        minPos   = copy.deepcopy(boxPos)

    lastIndex = len(boxPos) - 1
    while 1:
        index, blength = boxPos[lastIndex]
        if (index == 0 and blength == len(originData) - len(boxPos) + 1) or lastIndex < 0: return (minPos, minValue)
        if blength == 1:
            lastIndex -= 1
            continue
        else:
            boxPos[lastIndex] = (index + 1, blength - 1)
            if lastIndex >= 1:
                boxPos[lastIndex - 1] = (boxPos[lastIndex - 1][0], boxPos[lastIndex - 1][1] + 1)
            break

    return calBoxLength(originData=originData, boxPos=boxPos, minPos=minPos, minValue=minValue)


# print calBoxLength([1, 2, 3, 4], [(0, 1), (1, 3)], None, None)

def calSuatableKValue(originData):
    originDataLength = len(originData)
    minSSE = None
    minSSEPosition = list()
    for k in range(1, originDataLength):
        # 构造初始位置
        initPosition = list()
        if k > 1:
            initPosition = [(0, 1)]
            for index in range(1, k -1):
                initPosition.append((initPosition[index - 1][0] + initPosition[index - 1][1], 1))
            initPosition.append((initPosition[k - 2][0] + initPosition[k - 2][1], originDataLength - k + 1))
        else:
            initPosition = [(0, originDataLength)]

        minPos, minValue = calBoxLength(originData, initPosition, None, None)
        if minSSE == None or minValue < minSSE:
            minSSE = minValue
            minSSEPosition = copy.deepcopy(minPos)

    return minSSEPosition

# print calSuatableKValue([1, 3, 5, 7, 8, 9, 10])

def loadBox(originData):
    boxPos = calSuatableKValue(originData)
    print boxPos
    boxs = list()
    for index, length in boxPos:
        boxs.append(originData[index : index + length])
    return boxs

if __name__ == "__main__":
    datas = np.random.rayleigh(size=50)
    print(datas)
    print loadBox(datas)








# -*- coding: utf-8 -*-

def cleaningData(lines):
    """
    清除噪音数据
    :param lines: 数据行
    :return: 清理好的数据并且进行排序， [item, ...]
    """

    gdata = list()
    linesLength = len(lines)
    for index in range(linesLength):
        # 将偶数位为0的用1替换
        intitem = int(lines[index])
        if index % 2 == 1 and intitem == 0:
            intitem = 1
        gdata.append(intitem)

    gdata.sort()
    return gdata

# 等频的
def equalLengthSmooth(value):
    return value

def edgeSmooth(value):
    """
    使用箱边界进行光滑
    :param value:
    :return:
    """

    lastIndex = len(value) - 1
    if lastIndex <= 2: return value
    for index in range(1, lastIndex):
        leftDif  = value[index] - value[0]
        rightDif = value[lastIndex] - value[index]
        if leftDif < rightDif:
            value[index] = value[0]
        else:
            value[index] = value[lastIndex]
    return value


def avgSmooth(value):
    """
    使用平均值进行光滑
    :param value: list类型，需要进行平均的列表
    :return: [avg, ...]，与value同等长度的数组，值都未平均数
    """
    avgValue = float(sum(value)) / float(len(value))
    return [avgValue] * len(value)

def smoothDataSet(gdata, tlength = 10, smoothFuc = avgSmooth):
    """
    光滑数据
    :param gdata: 需要光滑的数据
    :param length: 桶长度
    :param smoothFuc: 需要使用的光滑函数
    :return: [t0: [d1, d2, ...], ...]
    """

    import math
    length = int(math.ceil(float(len(gdata)) / float(tlength)))

    gdataLength = len(gdata)
    smoothData = list()
    startIndex = 0
    while True:
        if startIndex + length < gdataLength:
            smoothData.append(smoothFuc(gdata[startIndex : startIndex + length]))
            startIndex += length
        else:
            sliceSD = gdata[startIndex : length]
            if len(sliceSD) > 0:
                smoothData.append(smoothFuc(sliceSD))
            break
    return smoothData

if __name__ == "__main__":
    import util.fileoperate as fop
    gdata = cleaningData(fop.getLines("../dataset/waitakere.txt"))
    # print(gdata)
    smoothFuncs = [equalLengthSmooth, avgSmooth, edgeSmooth]
    smoothFuncName = ["等频光滑", "平均值光滑", "箱边界光滑"]
    for fun, name in zip(smoothFuncs, smoothFuncName):
        print "\n\n" + "+" * 30 + "  使用" + name + "  " + "+" * 30 + "\n"
        print smoothDataSet(gdata=gdata, tlength=100, smoothFuc=fun)

























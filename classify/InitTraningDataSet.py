# -*- coding: utf-8 -*-

import util.fileoperate as fop
import dataelement as dtel

def loadTrainingData(fp):
    """
    加载数据
    :param fp: 文件路径
    :return: [label:col, ...]
    """
    lines = fop.getLines(fp)

    titles = list()
    initTrainingDatas = list()

    # 分割数数据集
    for index in range(len(lines)):
        items = lines[index].split("\t")
        if items.__contains__(""):
            items.remove("")
        if index == 0:
            titles = items
        else:
            initTrainingDatas.append(items)

    # 转化数据集
    trainingDatas = list() # [col, ...]
    maxTrainingDataLength = len(initTrainingDatas[0])
    for index in range(maxTrainingDataLength):
        cols = [row[index] for row in initTrainingDatas]
        trainingDatas.append(cols)

    trainingDataDic = dict()
    for key, value in zip(titles, trainingDatas):
        trainingDataDic[key] = value

    return trainingDataDic


def trainingDataSetDic(tds):

    # 去重属性值
    trainingDatas = dict()
    for key, value in zip(tds.keys(), tds.values()):
        trainingDatas[key] = set(value)

    # 标签化属性值
    labelTrainingDatas = dict()
    for key, value in zip(trainingDatas.keys(), trainingDatas.values()):
        labelCol = list()
        for index, item in zip(range(len(value)), value):
            ele = dtel.parse(item)
            ele.label = index
            labelCol.append(ele)
        labelTrainingDatas[key] = labelCol

    return labelTrainingDatas


def labelingTraingDataSet(dataSet, dataSetLabel):
    labelDS = dict()
    # 遍历训练集
    for prop in dataSet.keys():
        propertyValues = dataSet[prop]
        pv = list()
        dataEles = dataSetLabel[prop]

        # 遍历分类所对应的值
        for pvalue in propertyValues:
            # 转为为标签值
            for ele in dataEles:
                if ele.rawValue == pvalue:
                    pv.append(ele.label)
        labelDS[prop] = pv
    return labelDS




if __name__ == "__main__":
    tds = loadTrainingData("../dataset/Training-data.txt")
    # print tds
    tdsDic = trainingDataSetDic(tds)
    labelDS = labelingTraingDataSet(tds, tdsDic)
    for key, value in zip(labelDS.keys(), labelDS.values()):
        print key, " : ", value














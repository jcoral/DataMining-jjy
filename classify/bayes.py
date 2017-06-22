# -*- coding: utf-8 -*-

import dataelement as dtel
import InitTraningDataSet as itds


def transTestData(testData, trainingDataLabel):
    """
     将测试数据标签化
    :param testData: 需要测试的数据"age=12,income=123"
    :param trainingDataLabel: 记录类所对应的标签值
    :return: [class: label, ...]
    """
    items = testData.split(",")
    testDataDic = dict()
    for item in items:
        kv = item.split("=")
        for ele in trainingDataLabel[kv[0]]:
            if ele.isSameClass(kv[1]):
                testDataDic[kv[0]] = ele.label
    return testDataDic

class NBayes:

    def __init__(self, trainingDataSetFilePath):
        initTD = itds.loadTrainingData(trainingDataSetFilePath)
        self.trainingLabel = itds.trainingDataSetDic(initTD)
        self.trainingData  = itds.labelingTraingDataSet(initTD, self.trainingLabel)


    def pred(self, testDataStr, predClass):
        """
        对测试集进行分类
        :param testDataStr: "age=12,income=123"
        :param predClass:   需要预测的类别
        :return: (label, p) (分类标签，分类标签所对应的概率)
        """
        testData = transTestData(testDataStr, self.trainingLabel)
        # 分类所对应的所有训练集合
        classValues = self.trainingData[predClass]
        pdClassTimes  = dict() #  [label: times, ...] predClass类所有标签出现的次数

        # 遍历每一行数据
        classTimes = dict()    # [pdClassLabel: [class: [label: times], ...] predClass对应testData出现的次数
        for cvIndex in range(len(classValues)):
            cvValue = classValues[cvIndex]
            pdClassTimes[cvValue] = pdClassTimes.get(cvValue, 0) + 1

            # 对testData的类别进行计数
            for tdClass, tdLabel in zip(testData.keys(), testData.values()):
                ct = None
                if not classTimes.__contains__(cvValue):
                    ct = dict()
                    for key in testData.keys():
                        ct[key] = 0
                    classTimes[cvValue] = ct
                else:
                    ct = classTimes[cvValue]
                trainingDataLabelValue = self.trainingData[tdClass][cvIndex]
                if trainingDataLabelValue == tdLabel:
                    ct[tdClass] = ct[tdClass] + 1

        # 使用拉普拉斯法补充0项
        zeroItem = dict()
        for pdLabel, tdTimes in zip(classTimes.keys(), classTimes.values()):
            # exsitZero = False
            for k, v in zip(tdTimes.keys(), tdTimes.values()):
                if v == 0:
                    zeroItem[pdLabel] = k

        # 遍历predClass分类：classTimes
        trainingDataSetLength = sum(pdClassTimes.values())
        maxp = None # (classLabel, p)
        for pdClassLabel, prioriItems in zip(classTimes.keys(), classTimes.values()):
            curp = 1 # 先验概率

            # 遍历除predClass之外的
            for pk, pitem in zip(prioriItems.keys(), prioriItems.values()):
                frontValue = float(pitem)
                backValue  = float(pdClassTimes[pdClassLabel])

                # 判断该项出现的次数是否是0
                if zeroItem.__contains__(pdLabel):
                    if zeroItem[pdLabel] == pk:
                        frontValue += 1
                        backValue += len(self.trainingLabel[pk])
                curp *= frontValue / backValue
            curp *= float(pdClassTimes[pdClassLabel]) / float(trainingDataSetLength)
            if maxp == None or curp > maxp[1]:
                maxp = (pdClassLabel, curp)

        # print pdClassTimes
        # print classTimes
        # print maxp
        for ele in self.trainingLabel[predClass]:
            if ele.label == maxp[0]:
                maxp = (ele.rawValue, maxp[1])
        return maxp



if __name__ == "__main__":
    fp = '../dataset/Training-data.txt'
    nb = NBayes(fp)
    print nb.pred("age=26,income=medium,student=yes,credit_rating=fair","buys_computer")
    print nb.pred("age=32,income=high,student=no,credit_rating=fair","buys_computer")
    print nb.pred("age=42,income=medium,student=no,credit_rating=fair","buys_computer")















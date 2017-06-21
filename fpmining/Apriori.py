# -*- coding: utf-8 -*-


# 生产第一候选集
def generateFirstCandSet(originData):
    candSet = dict()
    def itemsIter(items):
        for item in items:
            candSet[item] = candSet.get(item, 0) + 1
    map(itemsIter, originData)
    return candSet


# 过滤候选集
def filterCandSet(candSet, minSupport):
    keys = candSet.keys()
    for key in keys:
        if candSet[key] < minSupport:
            del candSet[key]
    return candSet

# 生成频繁一项集
def generateFirstFreSet(originData, sup):
    return filterCandSet(generateFirstCandSet(originData), sup)

# 生成频繁项集
def generateFreSet(freSet, originData, minSupport):
    freSetKeys = freSet.keys()
    itemsLength = len(freSetKeys)
    allSet = dict()
    for h in range(itemsLength):
        for f in range(h + 1, itemsLength):
            # 合并两个项集
            hitemSet = set(freSetKeys[h].split(","))
            fitemSet = set(freSetKeys[f].split(","))
            itemSet  = hitemSet.union(fitemSet)

            # 查找itemSet出现的次数
            counter = 0
            for items in originData:
                if items.issuperset(itemSet):
                    counter += 1
            if counter >= minSupport:
                items = list(itemSet)
                items.sort()
                allSet[",".join(items)] = counter
    return allSet
    
# 主方法
def apriori_main(originData, minSupport, generateFunc = generateFreSet):
    """
    Apriori主函数
    :param originData: 初始数据[set1, set2, ...]
    :param minSupport: 0 ... 1
    :return: 频繁项集
    """

    supportTimes = minSupport * len(originData)
    firstFreSet  = generateFirstFreSet(originData, supportTimes)
    allFreSet    = firstFreSet.copy()
    freSet       = generateFreSet(firstFreSet, originData, supportTimes)
    while len(freSet.keys()) != 0:
        allFreSet.update(freSet)
        freSet = generateFunc(freSet, originData, supportTimes)

    return allFreSet

def loadAprioriData(precent = 0.5):
    import util.sampledata as sd

    filePath = "../dataset/retail.txt"
    lines = sd.simapleWithPrecent(filePath=filePath, precent=0.2)
    originData = list()
    for line in lines:
        ls = set(line.split(' '))
        ls.remove('')
        originData.append(ls)
    return originData


################  测试　####################

if __name__ == "__main__":


    print apriori_main(loadAprioriData(0.2), 0.1)


















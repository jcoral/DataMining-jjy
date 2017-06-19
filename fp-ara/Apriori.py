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
def apriori_main(originData, minSupport):
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
        freSet = generateFreSet(freSet, originData, supportTimes)

    return allFreSet


################  测试　####################

if __name__ == "__main__":
    # originData = [
    #                 set(["I1", "I2", "I5"]),
    #                 set(["I2", "I4"]),
    #                 set(["I2", "I3"]),
    #                 set(["I1", "I2", "I4"]),
    #                 set(["I1", "I3"]),
    #                 set(["I2", "I3"]),
    #                 set(["I1", "I3"]),
    #                 set(["I1", "I2", "I3", "I5"]),
    #                 set(["I1", "I2", "I3"])
    #                 ]

    import util.fileoperate as fop

    lines = fop.getLines("../dataset/retail.txt")
    originData = list()
    for line in lines:
        ls = set(line.split(' '))
        ls.remove('')
        originData.append(ls)

    print apriori_main(originData, 0.01)

















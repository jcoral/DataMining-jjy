# -*- coding: utf-8 -*-

import itertools

def comb(itemSet):
    """
    组合所有的关联项集
    :param itemSet: 频繁项集
    :return: [(frontItem, backItem), ...]
    """
    itemsSet = set(itemSet.split(","))
    itemsSetLength = len(itemsSet)

    allComb = list()
    for r in range(itemsSetLength):
        fontItems = list(itertools.combinations(itemsSet, r))
        for frontItem in fontItems:
            backItem = itemsSet - set(frontItem)
            if len(backItem) > 0 and frontItem != backItem:
                allComb.append((set(frontItem), backItem))

    return allComb


def generateASRule(freItemSet, min_con = 0.5):
    """
    生成关联规则
    :param freItemSet: [ItemSet: times, ...]频繁项集
    :param min_con: 最小置信度
    :return: [frontItem, backItem, con]
    """

    asItemSet = list()
    for itemSet, times in zip(freItemSet.keys(), freItemSet.values()):

        #　组合所有的项集
        allComb = comb(itemSet)
        if len(allComb) <= 0: continue
        # print allComb

        # 求置信度
        # fontItem => backItem
        for frontItem, backItem in allComb:
            # 将item转为list类型并排序
            frontItemList  = list(frontItem)
            backItemList   = list(backItem)
            frontItemList.sort()
            backItemList.sort()

            # 查找前项和后项出现的次数
            frontItemTimes = float(freItemSet.get(",".join(frontItemList), 0))
            backItemTimes  = float(freItemSet.get(",".join(backItemList), 0))

            # 查找前项和后项组合后的次数
            newItems = list(set(frontItem).union(set(backItem)))
            newItems.sort()
            newItemsTimes = freItemSet.get(",".join(newItems), 0)

            # 计算置信度
            if frontItemTimes != 0:
                con = newItemsTimes / frontItemTimes
                if con >= min_con:
                    asItemSet.append([frontItemList, backItemList, con])
    return asItemSet

def printAsRule(asItems):
    for item in asItems:
        print ",".join(item[0]), " => ", ",".join(item[1]), "  con = ", item[2]



if __name__ == "__main__":

    import Apriori
    freItemSet = Apriori.apriori_main(Apriori.loadAprioriData(0.2), 0.01)

    asItems = generateASRule(freItemSet, min_con=0.3)
    printAsRule(asItems)


















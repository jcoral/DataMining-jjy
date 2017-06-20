# -*- coding: utf-8 -*-

import hashlib


def generateFreItemSet(freItemSet, originData, minSupport):
    """
    使用hash求频繁项集
    :param freItemSet: [i1, i2, ...] 频繁项集
    :param minSupport: 最小支持度
    :return: [item: times, ...]
    """

    # [md5(item): [item: times, item: times, ...]]
    box = dict()

    # 组合所有的候选集
    itemsLength = len(freItemSet)
    allCandItemSet = list()
    for h in range(itemsLength):
        for f in range(h + 1, itemsLength):
            # 合并两个项集
            hitemSet = set(freItemSet[h].split(","))
            fitemSet = set(freItemSet[f].split(","))
            itemSet  = hitemSet.union(fitemSet)
            allCandItemSet.append(itemSet)

    # 遍历数据集
    # 如果候选项集在事务当中，则将候选集添加到桶中
    for itemSet in originData:
        for candItem in allCandItemSet:
            if candItem.issubset(itemSet):
                candItemList = list(candItem)
                candItemList.sort()
                candItemStr = ",".join(candItemList)

                md5 = hashlib.md5()
                md5.update(candItemStr)
                candItemMD = md5.hexdigest()

                boxItems = box.get(candItemMD, dict())
                boxItems[candItemStr] = boxItems.get(candItemStr, 0) + 1
                box[candItemMD] = boxItems

    # 过滤小于支持度的的项集
    boxKeys = box.keys()
    allFreItemSet = dict()
    for key in boxKeys:
        # 如果整个桶的长度小于支持度。则删除掉
        if sum(box[key].values()) >= minSupport:
            boxItems = box.get(key)
            boxItemsKeys = boxItems.keys()
            for boxItemsKey in boxItemsKeys:
                candItemTimes = boxItems[boxItemsKey]
                if candItemTimes >= minSupport:
                    allFreItemSet[boxItemsKey] = candItemTimes
                else:
                    boxItems.__delitem__(boxItemsKey)
        else:
            box.__delitem__(key)

    return allFreItemSet


if __name__ == "__main__":

    import Apriori as apriori

    originData = [
        set(["I1", "I2", "I5"]),
        set(["I2", "I4"]),
        set(["I2", "I3"]),
        set(["I1", "I2", "I4"]),
        set(["I1", "I3"]),
        set(["I2", "I3"]),
        set(["I1", "I3"]),
        set(["I1", "I2", "I3", "I5"]),
        set(["I1", "I2", "I3"])
    ]
    freFirstItemSet = apriori.generateFirstCandSet(originData)


    print generateFreItemSet(freFirstItemSet.keys(), originData, 2)













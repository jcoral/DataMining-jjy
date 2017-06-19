# -*- coding: utf-8 -*-

def fillEmpty(originData):
    """
    填充空的数据
    :param originData: 初始数据, [line,...]
    :return: [[lineItem,...], ...]
    """
    # 存放文件所有的数据
    allLine = list()
    for row in originData:
        # 分割每一行的数据
        _items = row.split("\t")

        import math
        # 标识当前行是否需要填充
        needFill = False
        items = list()
        for item in _items:
            # 判断是否是整数
            # 整数不包含.
            if str(item).__contains__('.'):
                items.append(math.fabs(float(item)))
            else:
                needFill = True

        if len(items) <= 0: continue

        # 填充缺失值
        if needFill:
            # 求平均值
            avgItems = round(float(sum(items)) / float(len(items)), 1)
            items = list()

            # 填充缺失值
            for item in _items:
                if float(item) < 0:
                    items.append(avgItems)
                    continue
                if not item.__contains__('.'):
                    items.append(avgItems)
                else:
                    items.append(float(item))

        # 添加items到总的当中去
        allLine.append(items)
    return allLine

if __name__ == "__main__":
    filePath = "../dataset/noise-data-1.txt"
    import util.fileoperate as fop
    lines = fop.getLines(filePath)
    d = fillEmpty(lines)
    fop.saveAsFileWithList(d, "./data.txt")




















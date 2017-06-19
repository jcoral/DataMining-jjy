# -*- coding: utf-8 -*-

def getLines(fp):
    """
    获取文件所有的行
    :param fp: 文件路径
    :return: [line, ...]
    """

    targetFile = open(fp)
    _lines = targetFile.readlines()
    targetFile.close()
    lines = list()
    for line in _lines:
        if line.lower() == '\\n':
            continue
        lines.append(line.replace("\n", ""))
    return  lines


def saveAsFileWithList(list1, fp, sep = " ", endSep = "\n"):
    """
    存放列表
    :param list1: 需要存放的文件, 二维数组
    :param fp: 文件路径
    :param sep: 每一个元素的分隔符
    :param endSep: 每一项的结尾分隔符
    """

    targetFile = open(fp, mode="w")
    for row in list1:
        targetFile.write(sep.join([ str(v) for v in row]) + endSep)

























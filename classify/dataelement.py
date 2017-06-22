# -*- coding: utf-8 -*-

DEqual = "="
DLess  = "<"
DEqLess  = "<="
DGreater = ">"
DEqGreater = ">="
DSection   = "..." # 闭区间
DLSection  = "=.." # 左闭右开
DRSection  = "..=" # 左开右闭
DContainer = ","   # 存在

def parse(ele):

    # if ele[0] == DEqual:
    #     return DataElement(value=float(ele).replace(DEqual, ""), type=DEqual)

    if ele[0] == DLess and ele[1] != DEqual:
        return DataElement(value=float((ele).replace(DLess, "")), type=DLess, rawValue=ele)

    if ele[0: 2] == DEqLess:
        return DataElement(value=float((ele).replace(DEqLess, "")), type=DEqLess, rawValue=ele)

    if ele[0] == DGreater and ele[1] != DEqual:
        return DataElement(value=float((ele).replace(DGreater, "")), type=DGreater, rawValue=ele)

    if ele[0: 2] == DEqGreater:
        return DataElement(value=float((ele).replace(DEqGreater, "")), type=DEqGreater, rawValue=ele)

    _ele = str(ele).replace("\t", "")
    sections = _ele.split(DSection)
    if len(sections) == 2:
        return DataElement(value=(float(sections[0]), float(sections[1])), type=DSection, rawValue=ele)

    dlSections = _ele.split(DLSection)
    if len(dlSections) == 2:
        return DataElement(value=(float(sections[0]), float(sections[1])), type=DLSection, rawValue=ele)

    drSection = _ele.split(DRSection)
    if len(drSection) == 2:
        return DataElement(value=(float(sections[0]), float(sections[1])), type=DRSection, rawValue=ele)

    items = _ele.split(DContainer)
    if items.__contains__(None): items.remove(None)
    return DataElement(value=tuple(items), type=DContainer, rawValue=ele)
class DataElement():

    def __init__(self, value = None, type = None, rawValue = None):
        self.value = value
        self.type  = type
        self.label = None
        self.rawValue = rawValue

    def isSameClass(self, value):
        if self.type == DEqual:    return self.value == float(value)
        if self.type == DLess:     return float(value) < self.value
        if self.type == DEqLess:   return float(value) <= float(self.value)
        if self.type == DGreater:  return float(value) > self.value
        if self.type == DEqGreater:return float(value) >= self.value
        if self.type == DSection:  return float(value) >= self.value[0] and float(value) <= self.value[1]
        if self.type == DLSection: return float(value) >= self.value[0] and float(value) < self.value[1]
        if self.type == DRSection: return float(value) >  self.value[0] and float(value) <= self.value[1]
        if self.type == DContainer:return self.value.__contains__(value)
            

    def __str__(self):
        return "Type: " + self.type + " Value: " + str(self.value) + " Label: " + str(self.label)

#
# e1 = parse("asd,123")
# print e1.isSameClass("123")












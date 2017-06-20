# -*- coding: utf-8 -*-

import random
def simapleWithPrecent(originData = None, filePath = None, precent = 0.5):
    if filePath != None and originData == None:
        import util.fileoperate as fop
        originData = fop.getLines(filePath)
    return random.sample(originData, int(len(originData) * precent))



def simaleWithUseRand(originData = None, fp = None):
    if originData == None and fp != None:
        import util.fileoperate as fop
        originData = fop.getLines(fp)

    import random
    sampleData = list()
    for item in originData:
        if random.randint(0, 2) == 1:
            sampleData.append(item)
    return sampleData

def simaleWithUseNB(originData = None, fp = None, precent = 0.5):
    if originData == None and fp != None:
        import util.fileoperate as fop
        originData = fop.getLines(fp)

    import scipy.stats as sstats
    print sstats.bernoulli(originData, len(originData), precent)

# simaleWithUseNB([1, 2, 3, 4, 5,6, 12,312,3])
# print simaleWithUseNB(originData=[1, 3, 4, 6, 123])








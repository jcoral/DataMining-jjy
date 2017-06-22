# -*- coding: utf-8 -*-

import hashlib
import itertools
md5 = hashlib.md5()
md5.update('123')
print md5.hexdigest()

md51 = hashlib.md5()
md51.update('123')
print md51.hexdigest()

from classify.dataelement import DataElement

dm = "asdasd123"

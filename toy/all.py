#!/usr/bin/env python
#coding:utf-8
#统计各种言语的代码行数

import os
from collections import defaultdict

d = defaultdict(int)

for dirpath, dirname, filenames in os.walk('.'):
    for filename in filenames:
        path = os.path.join(dirpath, filename)
        ext = os.path.splitext(filename)[1]
        d[ext] += len(list(open(path)))

for ext, n_lines in d.items():
    print ext, n_lines

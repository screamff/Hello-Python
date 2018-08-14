#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import json
import re

if len(sys.argv)>2:
    with open(sys.argv[1], 'r') as f:
        data = json.load(f)
    with open(sys.argv[2], 'r') as f:
        raw_doc = f.read()
else:
    print 'usage:python translator.py items.json refiner.html'

for i in data.iterkeys():
    raw_position = re.compile(r">" + (i) + r"<")
    raw_doc = raw_position.sub('>'+data[i].encode('utf-8')+'<', raw_doc)

with open('translated.html', 'w') as f:
    f.write(raw_doc)

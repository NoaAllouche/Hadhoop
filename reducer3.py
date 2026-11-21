#!/usr/bin/env python3

from itertools import groupby
from operator import itemgetter
import sys

results = []

data = (line.rstrip().split('\t', 1) for line in sys.stdin)

for word, group in groupby(data, itemgetter(0)):
    total_count = sum(int(count) for _, count in group)
    results.append((word, total_count))

results.sort(key=itemgetter(1), reverse=True)

for word, count in results[:3]:
    print('%s\t%d' % (word, count))

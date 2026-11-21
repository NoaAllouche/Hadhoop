#!/usr/bin/env python3
import sys

for line in sys.stdin:
    for word in line.split():
        word = word.lower().rstrip('.,')
        if word:
            print('%s\t%d' % (word, 1))

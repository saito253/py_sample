#!/usr/bin/python3

import subprocess

with open('sample.txt', 'r') as f:
    for line in f:
        print(line)

ret = subprocess.call('ls')
print(ret)

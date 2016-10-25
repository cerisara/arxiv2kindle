import glob
import sys
import re

fs = glob.glob(sys.argv[1]+'/**/*.txt')
for f in fs:
    with open(f,'r') as f: ls = f.readlines()
    for l in ls:
        m=re.search('\d\d\d\d.\d\d\d\d\d',l)
        if not m==None: print(m.group(0))


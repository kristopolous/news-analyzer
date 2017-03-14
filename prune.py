#!/usr/bin/python

import glob
import hashlib
import re
import os

digest = {}
ulinkCount = 0
fileList = glob.glob('./feeds/1*')
for d in sorted(fileList):
    for feed in glob.glob('%s/*' % d):
        newdigest = hashlib.md5(open(feed, 'rb').read()).hexdigest()

        name = re.split('/', feed)[-1]
        uniq = "%s:%s" % (name, newdigest)
        if not uniq in digest:
            digest[uniq] = 1
        else:
            digest[uniq] += 1
            ulinkCount += 1
            print feed
            os.unlink(feed)

print ulinkCount
    

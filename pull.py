#!/usr/bin/python3

import json
import time
import os
import requests
import re

now = int(time.time())
basepath = 'feeds/%d/' % now
os.mkdir(basepath)

def stub(what):
    return re.sub(' ', '_', what).lower()

with open('sitelist.json', 'r') as sitelist:
    siteMap = json.load(sitelist)
    for site in siteMap:
        if not site['rss']:
            continue

        print("%s: %s" %(site['name'], site['rss']) )
        data = str(requests.get( site['rss'] ).content)
        path = "%s%s" % (basepath, stub( site['name'] ))

        with open(path, 'w') as f:
             f.write(data)



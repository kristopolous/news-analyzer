#!/usr/bin/python3

import json
import time
import os
import requests
import re

now = int(time.time())
basepath = 'feeds/%d/' % now
os.mkdir(basepath)

epMap = {
    'xml': 'rss',
    'html': 'site'
}

def stub(what):
    return re.sub(' ', '_', what).lower()

def get(url):
    return requests.get( url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'} ).content

print(now)
with open('sitelist.json', 'r') as sitelist:
    siteMap = json.load(sitelist)
    for site in siteMap:
        if not 'name' in site:
            continue

        if site['name'] == "STOP":
            break

        for ext, key in epMap.items():
            if key not in site:
                continue

            url = site[key]
            try:
                print("%s: %s" %(site['name'], url) )
                data = get( url )
                path = "%s%s.%s" % (basepath, stub( site['name'] ), ext)

                with open(path, 'wb') as f:
                     f.write(data)
            except:
                pass


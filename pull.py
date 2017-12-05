#!/usr/bin/python3

import json
import time
import os
import requests
import re
import json
import xml.etree.ElementTree

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
    return requests.get( url, headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:53.0) Gecko/20100101 Firefox/53.0'} )

def article_get(url):
    pass

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
                data = get( url ).content
                path = "%s%s.%s" % (basepath, stub( site['name'] ), ext)

                with open(path, 'wb') as f:
                    f.write(data)

                if key == 'rss':
                    articleList = []
                    e = xml.etree.ElementTree.parse(path).getroot()
                    for item in e.iter('item'):
                        link = item.find('link')
                        response = get(link.text)
                        articleList.append([response.url, response.text])

                    path = "%s%s.%s" % (basepath, stub( site['name'] ), "articles")
                    with open(path, 'w') as f:
                        json.dump(articleList, f)
 
            except Exception as ex:
                print("exception", ex, path, url)
                pass


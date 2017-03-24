#!/usr/bin/python
import hashlib
import binascii
import sqlite3
import glob
import os
from lxml import etree
from StringIO import StringIO

connMap = {}

def additem(unix_ts, source, md5, text):
    global connMap

    if source not in connMap:
        db_path = './feeds/rss-aggregate/%s.sql' % source;
        make_tables = not os.path.exists(db_path)
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        if make_tables:
            c.execute("create table articles(ts integer, md5 text unique, content text)")
            conn.commit()

        connMap[source] = (c, conn)

    c, conn = connMap[source]
    try:
        c.execute('insert into articles values(?, ?, ?)', [int(unix_ts), md5, text])
    except:
        pass


fileList = glob.glob('./feeds/1*')
for d in sorted(fileList):
    unix_ts = d.split('/')[-1]
    for feed_path in glob.glob('%s/*xml' % d):
        source = feed_path.split('/')[-1][:-4]
        handle = open(feed_path)
        data = handle.read()

        try:
            root = etree.parse(StringIO(data))
        except:
            print "no parse", feed_path
            next

        itemList = root.findall('.//item')

        if len(itemList) > 0:
            for x in itemList:
                item = etree.tostring(x)
                md5 = hashlib.md5(item).hexdigest()
                md5 = binascii.b2a_base64(md5.decode('hex')).strip('=\n')
                additem(unix_ts=unix_ts, source=source, md5=md5, text=item)

            handle.close()
            
        else:
            print "oh no", feed_path
            handle.close()

for c, conn in connMap.values():
    conn.commit()
    conn.close()

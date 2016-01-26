# coding: utf-8

import urllib
import sys

def schedule(data, block, file):
    """
    file: 远程文件的大小
    data: 已下载的数据大小
    block: 数据块的大小
    """
    per = int(100*data*block/file)
    if per > 100:
        per = 100
    # sys.stdout.write('%2d%%' % per)
    # sys.stdout.write('\b\b\b')
    # sys.stdout.flush()
    print "%2d%%" % per,
    print '\b\b\b',
    sys.stdout.flush()

url = 'https://baidu.com/'
local = '/tmp/baidu.html'

print "download file(baidu.html)... ",
urllib.urlretrieve(url, local, reporthook=schedule)

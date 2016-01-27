requests 库
===
HTTP for Humans. 相比于urllib, urllib2, requests是继承自urllib3的,
同时提供了更加简单、人性化API。

    >>> import requests
    >>> r = requests.get('https://api.github.com/user', auth=('neo1218', 'password'))
    >>> r.status_code
    200
    >>> r.headers['content-type']
    'application/json; charset=utf8'
    >>> r.encoding
    'utf-8'
    >>> r.text
    >>> r.json()

## requests 库的使用

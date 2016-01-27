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

1. **发送请求**
    + requests 的API是非常明确的, 直接暴露http方法
        + requests.get(put, delete, post, head, options)

2. **传递url参数**
    ````
    >>> user_pass = {'username':'neo1218', 'password':'1234'}
    >>> r = requests.get('https://api.github.com/users', params=user_pass)
    ````


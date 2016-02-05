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

3. **响应内容**
    + 读取服务器响应的内容
        ````
        >>> import requests
        >>> r = requests.get("https://api.github.com/neo1218/following")
        >>> r.text
        >>> r.encoding
        >>> r.encoding = 'ISO-8859-1'  # 设定新的编码解析
        ````

    + 二进制响应内容
        + 可以以字节的方式访问请求响应体, 对于非文本请求,
          Requests会自动解码<code>gzip和deflate</code>传输编码的响应数据
        + 例如: 以请求返回的二进制数据创建一张图片
        ````
        >>> from PIL import Image
        >>> from StringIO import StringIO
        >>> i = Image.open(StringIO(r.content))
        >>> # 二进制的数据 --> stream --> 转码 --> 图片
        ````

    + JSON响应内容
        + Requests 内置有一个JSON解码器
        ````
        >>> import requests
        >>> r = requests.get('https://api.github.com/users/December1900/')
        >>> r.json()
        ````
        + 如果r出现错误, json()解码器也会根据相应的状态码报错

    + 原始响应内容
        + Requests还可以读取来自服务器的原始套接字响应
        ````
        >>> r = requests.get('https://api.github.com/users/neo1218', stream=True)
        >>> r.raw.read(10)
        ````
        + 当然, 一般情况下将文本流保存到文件
        ````
        with open(filename, 'wb') as fd:
            for chunk in r.iter_content(chunk_size):
                fd.write(chunk)
        ````

+ **定制请求头**
    + 只需要简单的给headers参数传递一个dict即可
    ````
    >>> import json
    >>> url = 'https://api.github.com/some/endpoint'
    >>> payload = {'some': 'data'}
    >>> headers = {'content-type': 'application/json'}
    >>> r = requests.post(url, data=json.dumps(payload), headers=headers)
    ````

+ **更加复杂的post请求**
    + requests 可以将数据字典自动编码为表单形式
    ````
    >>> payload = {'key1': 'value1', 'key2': 'value2'}
    >>> r = requests.post(url, data=payload)
    >>> r.text
    {
        ...
        "form": {
            "key1": "value1",
            "key2": "value2"
        }
    }
    ````
    + 单独的data_dict将会在请求时自动编码为表单
    + 传递到headers的data_dict(json编码)将会作为定制头部
    + 仅json编码的data_dict将直接发布出去

+ **POST一个文件**
    + 使用Requests上传文件很简单(files字典)
    ````
    >>> files = {'file': open(filename, 'rb')}
    >>> r = requests.post(url, files=files)
    ````

+ **响应状态码**
    + 直接获取响应状态码
    ````
    >>> r = request.get('https://api.github.com/users/neo1218')
    >>> r.status_code
    200
    ````
    + 语义化查询状态码
    ````
    >>> r.status_code == requests.codes.ok
    True
    ````
    + 依据状态码引发错误
    ````
    >>> bad_r = requests.get('https://httpbin.org/status/404')
    >>> bad_r.status_code
    404
    >>> bad_r.raise_for_status()
    引发 requests.exceptions.HTTPError: 404 Client Error
    ````

+ **响应头**
    + 我们可以以python字典形式查看服务器响应头
    ````
    >>> r.headers
    ````
    + 根据[RFC2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html)标准, HTTP头部是大小写不敏感的
    ````
    >>> r.headers.get('content-type')
    >>> r.headers.get('Content-Type')
    ````

+ **Cookies**
    + Requests库允许快速访问cookie
    ````
    >>> r = requests.get(url)
    >>> r.cookies['example_cookie_name']
    example_cookie_value
    ````
    + 还可以使用cookies参数发送cookies
    ````
    >>> cookies = dict(cookies_are='working')
    >>> r = requests.get(url, cookies=cookies)
    ````

+ **重定向与请求历史**
    + Response.history 是一个纪录重定向对象(按事件顺序从老到新排序)的列表
    +

+ **超时**


+ **错误和异常**


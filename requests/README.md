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
        # chunk 分块流下载


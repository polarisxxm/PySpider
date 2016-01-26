urllib 模块
===
urllib, urllib2模块都是python内置的接受url请求的相关模块

## urllib的使用

    >> import urllib
    >> # 以下代码会获取github的网页源码并打印
    >> urllib.urlopen('https://github.com/').read()

1. **urllib.urlopen(url[,data[,proxies]])** :
    - 返回一个表示远程url的类文件对象,
      然后像操作本地文件一样操作类文件对象获取数据
    - 参数:
        + url: 数据资源的路径
        + data: POST到url的数据(比如登录时的提交数据)
        + proxies: web代理
    - 对返回类文件对象的操作:
        + read(), readline(), readlines(), fileno(), close()
        + info(): 服务器返回的头信息(httplib.HTTPMessage)
        + getcode(): 获取http状态码
        + geturl(): 返回请求的url
    - 代码示例:

    ````
        >> import urllib
        >> url = "https://github.com/"
        >> data = urllib.urlopen(url)
        >> data.read()  # 返回url对应网页的源代码
        >> print data.info()  # 输出服务器响应头
        >> data.getcode()  # 返回状态码(200 ok)
        >> data.close()  # 关闭类文件对象
    ````

2. **urllib.urlretrieve(url[, filename[, reporthook[, data]]])** :
    + urlretrieve函数直接将远程数据下载到本地, 保存在路径为filename的文件中,
      返回一个包含两个对象的元组(filename, headers)
    + 参数:
        + url: 数据资源的标识
        + filename: 本地保存下载数据的路径(若缺省会生成临时文件)
        + reporthook: 回调钩子函数(可以用于显示下载进度)
        + data: post到url的数据
    + 代码示例(下载github的网页源码并存储到/tmp/github.html, 同时显示下载进度):
    ````
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
            sys.stdout.write("%2d%%" % per)
            sys.stdout.write("\b\b\b")
            sys.stdout.flush()

        url = 'https://github.com/neo1218'
        local = '/tmp/github.html'

        urllib.urlretrieve(url, local, reporthook=schedule)
    ````


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

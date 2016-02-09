BeautifulSoup
===

    bs4是一个html(xml)的解析库, 相当强大, 方便开发者从html中快速提取数据

## 使用:

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, "lxml")

### 1. 获取浏览结构化数据
<code>soup.title</code>:

    <title>this is title</title>

<code>soup.title.name</code>:
    
    <title>
    
<code>soup.title.string</code>:

    this is title
    
<code>soup.title.parent.name</code>: 

    <head>
    
<code>soup.p</code>:

    <p class="title"><b>this is title</b></p>
    
<code>soup.p['class']</code>:

    title
    
<code>soup.a</code>:

    <a class="github" href="https://github.com/neo1218">neo1218</a>
    
<code>soup.find_all('a')</code>

    "<a class="github" href="https://github.com/neo1218" id="user1">neo1218</a>"
    "<a class="github" href="https://github.com/zxc0328" id="user2">zxc0328</a>"
    "<a class="github" href="https://github.com/otocat" id="user3">otocat</a>"

<code>soup.find(id="user1")</code>:

    "<a class="github" href="https://github.com/neo1218" id="user1">neo1218</a>"

### 举个例子

    for link in soup.find_all('a'):
        print link.get('href')
    # https://github.com/neo1218
    # https://github.com/zxc0328
    # https://github.com/otocat


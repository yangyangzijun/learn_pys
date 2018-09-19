import urllib.request
keyword="hello"
url="http://www.baidu.com/s?wd="+keyword
req=urllib.request.Request(url)
file=urllib.request.urlopen(req)
local=open("F:\py/6.html","wb")
data=file.read()
local.write(data)
local.close()

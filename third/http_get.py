import urllib.request
keyword="王"
key_word=urllib.request.quote(keyword)
url="http://www.baidu.com/s?wd="+key_word
req=urllib.request.Request(url)
file=urllib.request.urlopen(req)
local=open("F:\py/6.html","wb")
data=file.read()
local.write(data)
local.close()

import  urllib.request
url="http://www.xicidaili.com/wn/"
headers=("User-Agent","Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36")


file=urllib.request.build_opener()
file.addheaders=[headers]
data=file.open(url).read()

local=open("F:\py/3.html","wb")
local.write(data)
local.close()


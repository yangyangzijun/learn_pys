import  urllib.request
import urllib.parse
url="http://code.upc.edu.cn/loginpage.php"
req=urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
data=urllib.request.urlopen(req).read()

local=open("F:\py/code.html",'wb')
local.write(data)
local.close()
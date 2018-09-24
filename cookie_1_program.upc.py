import  urllib.request
import urllib.parse
import  http.cookiejar
url="http://program.upc.edu.cn/login/index.php"
postdata=urllib.parse.urlencode({"username":"1607010411" ,"password":"1607010411"}).encode('utf-8')
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36')
cjar=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
file=opener.open(req)
data=file.read()

local=open("F:\py/99.html",'wb' )
local.write(data)
local.close()
url2="http://program.upc.edu.cn/course/view.php?id=334"

data2=urllib.request.urlopen(url2).read()
local2=open("F:\py/98.html",'wb'
           )
local2.write(data2)
local2.close()
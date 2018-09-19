import  urllib.request
import urllib.parse
url="http://www.iqianyue.com/mypost/"
postdata=urllib.parse.urlencode  ({ "name":"yangyang","pass":"ywtfywty"}).encode('utf-8')#
req=urllib.request.Request(url,postdata)
req.add_header('User-Agent',' Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36')

data=urllib.request.urlopen(req).read()
file=open("F:/py/3.html","wb")
file.write(data)
file.close()
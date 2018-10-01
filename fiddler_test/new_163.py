import  urllib.request
import http.cookiejar
url="http://news.163.com/photoview/00AO0001/2296721.html?from=ph_ss#p=DT1CPI036VVV0001NOS"
headrs={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
     "Accept-Encoding":"gzip,deflate,br",
       "Accept-Language": "zh-CN,zh;q=0.9",
        "User - Agent": "Mozilla / 5.0(Windows NT 6.3;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 69.0.3497.100Safari / 537.36",
"Connection": "keep-alive",
"Host": "news.163.com"
        }
head=[]
for key,value in headrs.items():

    item=(key,value)
    head.append(item)
print(head)
print(headrs)

cjar=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPHandler,urllib.request.HTTPCookieProcessor(cjar))
opener.addheaders=head
urllib.request.install_opener(opener)
data=urllib.request.urlopen(url).read()
print(data)







#print(html)
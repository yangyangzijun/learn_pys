import urllib.request
import http.cookiejar
import re
url="http://v.qq.com/x/cover/1wbx6hb4d3icse8.html"
header={"Accept": "*/*",
    "Accept-Encoding":"utf-8,gbk",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Referer": "https://v.qq.com/x/cover/1wbx6hb4d3icse8.html",
        "Connection": "keep-alive",
        "Host": "dp3.qq.com"
}
cjar=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
head=[]
for key,value in header.items():
    item=(key,value)
    head.append(item)
opener.addheaders=head
urllib.request.install_opener(opener)
html=urllib.request.urlopen(url).read().decode("gbk", errors="replace")
patt="4.+?7509"
list=re.compile(patt).findall(str(html))
print(list)



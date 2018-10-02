import urllib.request
import http.cookiejar
import re

url_list=[]

url="http://video.coral.qq.com/varticle/3008268170/comment/v2?callback=_varticle3008268170commentv2&orinum=10&oriorder=o&pageflag=1&cursor=0&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1538460325906%20HTTP/1.1"
header={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding":"gbk,utf-8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36",
        "Referer": "https://v.qq.com/x/cover/1wbx6hb4d3icse8.html",
        "Connection": "keep-alive",
        "Host": "v.qq.com",
        "Upgrade-Insecure-Requests": "1"
}
cjar=http.cookiejar.CookieJar()
opener=urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
head=[]
for key,value in header.items():
    item=(key,value)
    head.append(item)
opener.addheaders=head
urllib.request.install_opener(opener)
html=urllib.request.urlopen(url).read().decode('UTF-8')
patt='last":".+?"'
list_1=re.compile(patt).findall(html)
#url_second=str(list_1[len(list_1)][7:-1])
content_patt='"content":".*?"'
userlist_patt='"nick":".+?"'
content_list=re.compile(content_patt).findall(html)
userlist=re.compile(userlist_patt).findall(html)
for l in range(0,len(userlist)):
    print(str(userlist[l]))
    #print(eval("u'" + str(content_list[l][11:-1]) + "'"))


#url="GET /varticle/3008268170/comment/v2?callback=_varticle3008268170commentv2&orinum=10&oriorder=o&pageflag=1&cursor="+str(list_1[len(list_1)][7:-1])+"&scorecursor=0&orirepnum=2&reporder=o&reppageflag=1&source=9&_=1538460579899 HTTP/1.1"







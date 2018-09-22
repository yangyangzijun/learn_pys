#yum.iqianyue.com/proxy
import  urllib.request



def use_ip(act_ip,url):
    ip=urllib.request.ProxyHandler({'http':act_ip})
    opener=urllib.request.build_opener(ip,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)
    data=urllib.request.urlopen(url).read()
    return  data
act_ip="47.104.152.232:80"
data=use_ip(act_ip,"http://www.baidu.com")
print(len(data))
local=open("F:/py/8.html",'wb')
local.write(data)
local.close()
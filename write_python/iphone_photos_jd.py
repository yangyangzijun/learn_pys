import  urllib.request
import  urllib.error
import re
def craw(url,page):
    html=urllib.request.urlopen(url).read()
    html=str(html)
    part1="gl-warp clearfix.*page clearfix"
    result=re.compile(part1).findall(html)
    result=result[0]
    part2='img width="220" height="220" data-img="1" src="//img.+?\.jpg'
    imagelist=re.compile(part2).findall(result)
    x=11
    for imageurl in imagelist:
        imagename="F:\py\jd/"+str(page)+"_"+str(x)+".jpg"""
        imageurl="http://"+imageurl[49:]
        print(imageurl)
        try:
            urllib.request.urlretrieve(imageurl,filename=imagename)
            print(imagename)
        except urllib.error.URLError:
            print("error")
        x=x+1
for i in range(1,100):
    url="https://list.jd.com/list.html?cat=9987,653,655&page="+str(i)
    craw(url,i)
import  urllib.request
import  urllib.error
try:
    data=urllib.request.urlopen("http://www.baidu.com")
    print("ok")
except urllib.error.URLError as e:
    print(e.code)
    print(e.reason)



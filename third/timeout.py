import  urllib.request
for i in range(1,100):
    try:
        file=urllib.request.urlopen("http://yum.iqianyue.com",timeout=0.11)
        data=file.read()
        print(len(data))
    except Exception as e:
        print("error"+str(e))


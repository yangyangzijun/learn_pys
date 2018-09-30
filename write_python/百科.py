import  urllib.request
import  re
def craw(url):

    headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36")

    file = urllib.request.build_opener()
    file.addheaders = [headers]
    data = file.open(url).read().decode('utf-8')
    patt1="<h2>"+".+?"+"</h2>"
    patt2='<div class="content">'+".+?"+"</span>"
    list_na=re.compile(patt1,re.S).findall(str(data))
    list_name=[]
    for l in list_na:

        list_name.append(l[5:-6])
    list_wo=re.compile(patt2,re.S).findall(str(data))
    list_word=[]
    for l in list_wo:

        list_word.append(l[31:-8])

    list_print=[]
    for l in range(0,len(list_word)):
        list_print.append(list_name[l])
        list_print.append(list_word[l])
    for l in list_print:
        print(l)







url="http://www.qiushibaike.com/8hr/page/2/"
craw(url)
import requests
import  re
import json
from concurrent.futures import ThreadPoolExecutor

def getimg(url,num):
    print('===================================抓取第{}页图片================================'.format(num))
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    r = requests.get(url,headers=headers)
    html = r.text
    jsonobj = json.loads(html)
    data1 = jsonobj['data']
    i = 0
    for item in data1:
        i+=1
        if i<=30:
            url = item['thumbURL']
            file_name = url.split('/')[-1]
            img = requests.get(url,headers=headers).content
            with open('C:\\Users\\sddbook\\Desktop\\pics of baidu\\'+file_name,'wb') as f:
                print('正在保存图片：'+file_name)
                f.write(img)
        
def main():
    kw = input('请您输入关键字：')
    num = int(input('请您输入要抓取的页数：'))
    pool = ThreadPoolExecutor(max_workers=5)
    for i in range(1,num+1):
        a = 30*i
        path1 = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=&1580782165599='.format(kw,kw,a)
        pool.submit(getimg,path1,i)
    pool.shutdown()
main()

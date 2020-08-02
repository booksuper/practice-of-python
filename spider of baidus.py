import requests
import  re
import json
from concurrent.futures import ThreadPoolExecutor

def getimg(url,num,path2):
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
            with open(path2+file_name,'wb') as f:
                print('正在保存图片：'+file_name)
                f.write(img)
        
def main():
    print('脚本名：百度图片爬虫\n版本：1.0\n开发者:海里生火\n功能：根据用户需求自行爬取百度图片\n特别声明：此程序链接的是百度图片，如若用户恶意下载百度图片，自负法律责任！！！')
    print('使用说明：前两个参数简明易懂，不予赘述。这里重点说明保存路径的选择：\n第一，输入时请切换至英文模式，文件命名也请用英文，不然可能报错；\n第二，自己在电脑任意位置建立一个文件夹(也可用已有的文件夹），将该文件的绝对路径复制下来粘贴到保存路径中即可。\n若文件夹在桌面上可直接右键查看其属性，内有该文件夹路径。')
    print(r'路径格式举例：C:\Users\sddbook\Desktop\pics of baidu')
    kw = input('请您输入关键字：')
    num = int(input('请您输入要抓取的页数：'))
    path2 = (input(r'请您输入下载图片的保存路径:')+r'\ ')
    pool = ThreadPoolExecutor(max_workers=5)
    for i in range(1,num+1):
        a = 30*i
        path1 = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&hd=&latest=&copyright=&word={}&s=&se=&tab=&width=&height=&face=0&istype=2&qc=&nc=1&fr=&expermode=&force=&pn={}&rn=30&gsm=&1580782165599='.format(kw,kw,a)
        pool.submit(getimg,path1,i,path2)
    pool.shutdown()
main()

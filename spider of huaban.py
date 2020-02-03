import requests
import  re
import json

def getimg(url,num):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    r = requests.get(url,headers=headers)
    html = r.text
    startindex = re.search('\["pins"] = ',html).span()[1]  #获取json数据的起始字符的下标
    endindex = re.search('}}];',html[startindex:]).span()[1]+startindex-1 #获取json数据的结束字符的下标
    jsonstr = html[startindex:endindex] #截取json数据
    jsonobj = json.loads(jsonstr)
    pin_id = jsonobj[19]['pin_id']
    print('========================================抓取第{}页图片====================================='.format(num))
    for item in jsonobj:
        url = 'https://hbimg.huabanimg.com/'+item['file']['key']
        img = requests.get(url).content
        with open('C:\\Users\\sddbook\\Desktop\\pics of  huabanwang\\'+item['file']['key']+'.jpg','wb') as f:
            print('正在保存图片：'+item['file']['key'])
            f.write(img)
    return pin_id
    
def main():
    path1 = 'https://huaban.com/explore/chaiquan/'
    num = 3 #要抓取的页数
    for i in range(0,num):
        i+=1
        pin_id = getimg(path1,i)
        path1 = 'https://huaban.com/explore/chaiquan/?k650rl4x&max={}&limit=20&wfl=1'.format(pin_id)

main()









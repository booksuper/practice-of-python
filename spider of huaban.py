import requests
import  re
import json


def getimg(url,num):
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}
    r = requests.get(url,headers=headers)
    html = r.text
    #print(html)
#\[\"pins\"\]\ =\ 
    startindex = re.search('\["pins"] = ',html).span()[1]
    #print(startindex)
    endindex = re.search('}}];',html[startindex:]).span()[1]+startindex-1

    jsonstr = html[startindex:endindex]
    #print(jsonstr)
    jsonobj = json.loads(jsonstr)
    pin_id = jsonobj[19]['pin_id']
    print('========================================抓取第{}页图片====================================='.format(num))
    
    for item in jsonobj:
        url = 'https://hbimg.huabanimg.com/'+item['file']['key']
        #print(url)
        img = requests.get(url).content
        with open('C:\\Users\\sddbook\\Desktop\\pics of  huabanwang\\'+item['file']['key']+'.jpg','wb') as f:
            print('正在保存图片：'+item['file']['key'])
            f.write(img)
    
    return pin_id
    

def main():

    path1 = 'https://huaban.com/explore/chaiquan/'
    num = 3
    for i in range(0,num):
        i+=1
        pin_id = getimg(path1,i)
        #print(pin_id)
        path1 = 'https://huaban.com/explore/chaiquan/?k650rl4x&max={}&limit=20&wfl=1'.format(pin_id)

main()
#https://huaban.com/explore/beijingsucai?k64r10jx&max=690123469&limit=20&wfl=1







#https://hbimg.huabanimg.com/

#https://huaban.com/discovery/beauty/?k64nldi7&max=2952851343&limit=20&wfl=1
#https://huaban.com/discovery/beauty/?k64nldi8&max=2952844752&limit=20&wfl=1
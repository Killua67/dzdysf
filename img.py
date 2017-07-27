#!/usr/bin/eny python
# _*_coding:utf-8_*_
import requests
import re


def img(url):

    im = requests.get(url).content
    url = 'https://www.how-old.net/Home/Analyze?isTest=False&source=&version=www.how-old.net'

    data = {'file': im}
    r = requests.post(url, files=data)
    r = r.text.replace('\\', '')
    gender = re.findall('"gender": "(.*?)"', r)
    age = re.findall('"age": (.*?),', r)
    lists = zip(gender,age)
    result = []
    for i,j in lists:
        if i == 'Male':
            i = '男'
        else:
            i = '女'
        result.append({'sex':i,"age":j})

    return result

print (img('http://mmbiz.qpic.cn/mmbiz_jpg/hWWXn4JfVmia8Giatv3h0Ge82jdbAjOFF962Laiasl7Pu2Sx3qibdQzqTFFnpnFYPwuCuMwXXia7eHs9zb0nibsaFM2g/0'))

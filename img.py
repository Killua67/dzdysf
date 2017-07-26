#!/usr/bin/eny python
# _*_coding:utf-8_*_
import requests
import re


def img(url):

    im = requests.get(url).content
    url = 'https://www.how-old.net/Home/Analyze?isTest=False&source=&version=www.how-old.net'

    data = {'file': im}
    r = requests.post(url, files=data).content.replace('\\', '')
    gender = re.search(r'"gender": "(.*?)"rn', r)
    age = re.search(r'"age": "(.*?)"rn', r)
    if gender.group(1) == 'Male':
        gender = '男'
    else:
        gender = '女'

    datas = [gender, age.group(1)]

    return datas

# print img('http://mmbiz.qpic.cn/mmbiz_jpg/hWWXn4JfVmhPHlMmKcpm8ScicEePezMicEYq7k3IHQIQJwPzCukmhb5Tib2icDEr09EgpyibeppaQdRo8gNDR8xnHAw/0')

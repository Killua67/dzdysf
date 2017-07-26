#!/usr/bin/eny python
#_*_coding:utf-8_*_
import requests
import base64
import json
import time

def yanzhi(url):
    im = base64.b64encode(requests.get(url).content)

    url = 'https://kan.msxiaobing.com/Api/Image/UploadBase64'
    r = requests.post(url, data=im)
    j = json.loads(r.content)

    img_url = j["Host"] + j["Url"]
    url2 = 'https://kan.msxiaobing.com/Api/ImageAnalyze/Process?service=yanzhi&tid=fe28043604774d329509beaeb73d722a'
    # data = {
    #     'Content[imageUrl]': img_url,
    #     'CreateTime': time.time(),
    # }
    data = {
        'MsgId':      1501076234031,
        'CreateTime': time.time(),
        'Content[imageUrl]': img_url

    }
    print(data)
    r2 = requests.post(url2, data=data)

    print(r2.content)



yanzhi('http://mmbiz.qpic.cn/mmbiz_jpg/hWWXn4JfVmhPHlMmKcpm8ScicEePezMicEYq7k3IHQIQJwPzCukmhb5Tib2icDEr09EgpyibeppaQdRo8gNDR8xnHAw/0')
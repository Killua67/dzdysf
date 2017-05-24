#!/usr/bin/eny python
# _*_coding:utf-8_*_

import requests
import json


def talk(content, userId):
    url = 'http://www.tuling123.com/openapi/api';
    s = requests.session()
    d = {"key": "653fd927e9ad4b19bbbb58ac07545d9a", "info": content, "userid": userId}
    data = json.dumps(d)
    r = s.post(url, data=data)
    text = json.loads(r.text)
    if text['code'] == 10000:
        return text['text']
    else:
        return '机器人失踪啦  ... ...  /n 请稍后再试'


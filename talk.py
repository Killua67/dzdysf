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
    if text['code'] == 100000:
        return text['text']
    elif text['code'] == 200000:
        return text['text'] + '\n' + text['url']
    elif text['code'] == 302000:
        return text['text'] + '\n' + text['list'][0]['article'] + ':' + text['list'][0]['detailurl']
    elif text['code'] == 308000:
        return text['text'] + '\n' + text['list'][0]['name'] + ':' + text['list'][0]['detailurl']
    elif text['code'] == 40001:
        return '参数key错误'
    elif text['code'] == 40002:
        return '请求内容info为空'
    else:
        return '机器人失踪啦  ... ...   请稍后再试'

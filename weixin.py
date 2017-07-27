#!/usr/bin/eny python
#_*_coding:utf-8_*_
import web
import os
import hashlib
import time
from lxml import etree
from talk import talk
from img import img

class WeixinInterface:

    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)

    def GET(self):
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        token = "zhiyong"

        l = [token, timestamp, nonce]
        l.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, l)
        hashcode = sha1.hexdigest()

        if hashcode == signature:
            return echostr

    def POST(self):
        str_xml = web.data()
        xml = etree.fromstring(str_xml)
        msgType = xml.find("MsgType").text
        fromUser = xml.find("FromUserName").text
        toUser = xml.find("ToUserName").text

        userId = fromUser[0:15]
        #文本信息
        if msgType == "text":
            content = xml.find("Content").text
            if content == u"菜单":
                menu = u'哈哈哈哈，欢迎关注。公众号里面有个机器人，还有声音识别和图片审美 ～'
                return self.render.reply_text(fromUser, toUser, int(time.time()), menu)
            elif content == u'快递':
                return self.render.reply_text(fromUser, toUser, int(time.time()), u'你好，查水表！')
            else:
                text = talk(content, userId)
                return self.render.reply_text(fromUser, toUser, int(time.time()), text)

        #语音信息
        elif msgType == "voice":
            content = xml.find("Recognition").text
            text =  talk(content, userId)
            return self.render.reply_text(fromUser, toUser, int(time.time()), text)
        
        #图片信息
        elif msgType == 'image':
            picUrl = xml.find("PicUrl").text
            result = img(picUrl)
            content = u'图中识别出 %d 张人脸 \n'%(len(result))
            for i in content:
                return self.render.reply_text(fromUser, toUser, int(time.time()), type(i))
        else:
            return ''

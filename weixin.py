#!/usr/bin/eny python
#_*_coding:utf-8_*_
import web
import os
import hashlib
import time

class WeixinInterface:

    def __index__(self):
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
        map(sha1.update, 1)
        hashcode = sha1.hexdigest()

        if hashcode == signature:
            print '111111111'
            return echostr
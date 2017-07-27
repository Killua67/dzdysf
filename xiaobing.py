# coding=utf-8
import requests
import time
from bs4 import BeautifulSoup


class xiaoiceApi():
    def __init__(self):
        self.headers = {}
        self.loadheaders()

    def loadheaders(self):
        '''
            导入headers
        '''
        with open("./headers.txt") as headers:
            line = headers.readline().strip()
            while line:
                key = line.split(":")[0]
                self.headers[key] = line[len(key) + 1:]
                line = headers.readline().strip()

    def chat(self, input_strs):
        '''
        聊天

            args (str):   
                input_strs  问题  
            return (dict):  
                status      状态  
                text        内容        
        '''
        if not self.headers:
            return self.dicts("error", "请打开浏览器 复制并将headers放入headers.txt中")
        data = {
            'location': 'msgdialog',
            'module': 'msgissue',
            'style_id': 1,
            'text': input_strs,
            'uid': 5175429989,
            'tovfids': '',
            'fids': '',
            'el': '[object HTMLDivElement]',
            '_t': 0,
        }

        try:
            url = 'http://weibo.com/aj/message/add?ajwvr=6'
            page = requests.post(url, data=data, headers=self.headers)
            # self.savePage(page.text, "./tmpPostPage.txt")
            if page.json()['code'] == '100000':
                text = self.loop(input_strs)
                return self.dicts("succeed", text)
            else:
                return self.dicts("failed", page.json()['msg'])
        except Exception as e:
            return self.dicts("error", e)

    def dicts(self, status, text):
        '''
            包装return
        '''
        return {"status": status, "text": text}

    def loop(self, input_strs):
        '''  
            刷新直到获取到回答
        '''
        times = 1
        while times:
            times += 1
            response = requests.get("http://weibo.com/aj/message/getbyid?ajwvr=6&uid=5175429989&count=1&_t=0",
                                    headers=self.headers)
            # self.savePage(response.text, "./tmpResponse.txt")
            soup = BeautifulSoup(response.json()['data']['html'], "lxml")
            text = soup.find("p", class_='page').text
            if cmp(text.encode("utf-8"),input_strs) <0 or times > 20:
                break
            time.sleep(0.3)
        return text

    # def savePage(self, text, file):
    #     with open(file, "w") as f:
    #         f.write(text)

# if __name__ == '__main__':
#     xb = xiaoiceApi()
#     print(xb.chat('嗯啊'))
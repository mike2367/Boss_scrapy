# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
# optional ip list
# from .settings import ip_list
import requests
import execjs
from .items import BossItem
from boss.other_src.Useragents import ua_list

class BossSpiderRandomUAMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(ua_list)
        request.headers['User-Agent'] = ua
        return None

# optional ip list
# class BossSpiderRandomProxyMiddleware(object):
#     def process_request(self, request, spider):
#         proxy = random.choice(ip_list)
#         request.meta['proxy'] = proxy

#          # close TCP connection each time and force to switch IP
#         request.headers['Connection'] = "Close"
#         return None

# cookie

class BossSpiderRandomCookieMiddleware(object):
    
    def process_request(self, request, spider):
        cookie = self.get_cookies()
        request.cookies = cookie
        return None
    
    def get_cookies(self):
        with open('boss/other_src/zp_token.js', 'r', encoding='utf-8') as f:
            jscode = f.read()
        # seed = requests.get("https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101020100&page=1").json()
        # seed = seed["zpData"]['seed']
        # print(seed)
        # 
        # try:
        #     json_ = requests.get("https://www.zhipin.com/wapi/zpgeek/search/joblist.json?scene=1&query=&city=101020100&page=1").json()
        #     seed = json_["zpData"]['seed']
        #     print(seed)
        # except Exception as e:
        #     print(json_)
        #     seed = "BzOGHKTzgpG7UJkhwCJyEwmOoLxFhkchUSq6PArYXrJfAXdA+AsHDQ7klUJo/Qxkaeo07L1Td1RtCWCs1b59yA=="
        # zp_stoken = execjs.compile(jscode).call('(new e).z', "PKTVe1hIwoHfKRy5nKZRelRjiF5W+//9yD7lo1O9JvA=")
        # TODO replace the token
        zp_stoken = "dbc3fw4zDuBUZQ2lhZRgVw4LDgcKGeHh3dmNiUXxRXsOAwq1dXsKqwofCtGBYX8K1wrTDiUzCjcKxwpdlw79OwptTw73DicOKdMOwWsK2VcKgxKHEh8SoxbTCo8Kjw4PCpD02DxMNEhEbFxkWFRQYEwwPGRUbFBcPEw0SEUI3w73ClcOBQD1GQjNWWlQQV2dkTWVTDV5MUUFDXhJpXEM5PUJBP8OJwqjCv8OUw4XCpsOAw5fDi8Kqwr8oQkk%2FQ8OCwqwsLcK8w7AzUBPCvHIOw4HDmw%2FCvcO%2FDcOPacOUw5Jmwr%2FCvTk8P8K%2FxYJGPSNFPEJLPkBLQj0zQGHDjWjDmMOPZMK9wrMuPxxKPT5JPkI9Pks8RDE%2BRxEsPUEvSBIVDBgZM0jCvcOCw4PDpT0%2B"


        cookie_string = 'wd_guid=544d13f9-f072-4fdc-9989-84452f1ecd52; historyState=state; _bl_uid=XtlO5cqLjv05qpj3t0d0nna8msI4; \
        lastCity=101020100; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1673095377,1673165470,1673257271,1673333037; \
        boss_login_mode=sms; __fid=c58f56b0daac21ec5273e9b4b258f537; \
        wt2=DY4IX_Pe18l5jPqD0AYgnA-G9UnTNtDaZ_zMhCpK7UovHjn5bKxYiZ6NtwTrfsFzsgpxFtIBCopvwd7HdvXTGrg~~; wbg=0; \
        __zp_stoken__={}; \
        geek_zp_token=V1RN0kEOL031ZiVtRvyB4bLCuw6zrQxCo~; __l=l=%2Fwww.zhipin.com%2Fshanghai%2F&r=&g=&s=3&friend_source=0&s=3&friend_source=0; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1673349533; __c=1673333037; __a=68265253.1672926940.1673257271.1673333037.431.9.106.431'.format(zp_stoken)

            # Handle potential ValueError by filtering out invalid cookie pairs
        cookie = dict(pair.strip().split('=', 1) for pair in cookie_string.split(';') if '=' in pair)
        return cookie



# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import time
import random
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
from .settings import ua_list, ip_list

class BossSpiderRandomUAMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(ua_list)
        request.headers['User-Agent'] = ua
        return None


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
        cookie_string="Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1726382937,1727087389,1727271878; __g=-; HMACCOUNT=9C1666AEF16C9008; wbg=0; zp_at=cyCNJ2R9aLN4qFoi1xpLhqD0lJ-MLWqX4f_D8qZi-Z4~; wt2=DBRbFh04aIVhsdSwlCA4cMdr9_C7UaRw4Ih9COYUWJlsASqhF9KhB41447E4OuaoAYNFRGdOcY4Yf5mEdM_zDTg~~; __zp_seo_uuid__=fc4c2353-02e4-4a6a-b0e0-55cee2bfd2f0; __l=r=https%3A%2F%2Fwww.bing.com%2F&l=%2F&s=1; lastCity=101020100; \
        __zp_stoken__=e468fNT3DocKzwrTCtDojEhARCwY%2BJzg9Kjc%2FNTFCOjs1PTQ4PTU9PBo3JXLCtA9%2Bw5Jaw4knNio9NDs2NTc0OkEaPUDEtMK3Nj4tEsK2DHXDj13DhwQEBWwDwozDgAXDk8K3J8OrwrQmJMKmwr05Mz84E8K1wqDDgcOLwrvCnsK9w4zCs8KTwr8zNzhALzdUYQ1WNzdJT1YFSV1QXFtNCkdSTCk4OTM6wrfCjcSALTgNDgYLEQMEDAUHERIKBAoQDwcSDAcIEAkDLjXCmsK5wpxFwoPElsO9xJnCmMKjw7DDgMO4Q8KtwqDCssK%2FwpXCqsKTwrDCqcKrwpvCusKWwq3DgUbCnsK6wrdFTcK8WsKmT1nCuHHCpsOCU0zCgkRfbGVvDQsMCmI3DxXCvQ%3D%3D; \
        Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1727416636; __c=1727405176; __a=98957338.1727405176..1727405176.10.1.10.10; \
        bst=V2R9whGOX_3l1pVtRuzRUZLC-47DrRzCo~|R9whGOX_3l1pVtRuzRUZLC-47DrTwSQ~"
            # Start Generation Here
            # Handle potential ValueError by filtering out invalid cookie pairs
        cookie = dict(pair.strip().split('=', 1) for pair in cookie_string.split(';') if '=' in pair)
        return cookie



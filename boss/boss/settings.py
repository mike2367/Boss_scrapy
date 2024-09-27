# Scrapy settings for boss project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "boss"

SPIDER_MODULES = ["boss.spiders"]
NEWSPIDER_MODULE = "boss.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "boss (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "boss.middlewares.BossSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "boss.middlewares.BossSpiderRandomUAMiddleware": 543,
#    "boss.middlewares.BossSpiderRandomProxyMiddleware": 544,
   "boss.middlewares.BossSpiderRandomCookieMiddleware": 545,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "boss.pipelines.mysqlPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

ua_list = ['Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
           'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36',
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11',
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
           'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0']

# Top-level
ip_list = [
    "174.211.146.2:3128",
    "72.161.129.217:8081",
    "131.243.36.241:8888",
    "105.13.255.37:8081",
    "216.78.146.134:1337",
    "214.32.171.207:1337",
    "74.243.166.85:80",
    "27.61.141.100:8888",
    "199.61.3.13:80",
    "113.99.77.94:8081",
    "66.189.250.230:8080",
    "142.46.255.163:1080",
    "133.179.143.92:80",
    "219.53.187.31:3128",
    "203.30.168.118:3128",
    "236.125.138.26:80",
    "130.114.79.189:8888",
    "119.4.197.59:8080",
    "221.214.236.194:8080",
    "131.32.51.232:8888",
    "26.20.55.224:3128",
    "122.134.103.200:1080",
    "144.59.88.107:80",
    "191.114.21.172:1080",
    "6.74.119.62:8081",
    "107.235.89.146:1080",
    "116.3.199.33:1080",
    "249.254.202.39:80",
    "222.254.224.151:3128",
    "250.143.157.10:1080",
    "167.244.206.115:3128",
    "103.167.59.63:1337",
    "61.175.177.12:8081",
    "215.53.58.63:1080",
    "79.88.166.1:80",
    "96.121.49.106:8081",
    "152.230.149.249:80",
    "33.26.246.43:8080",
    "215.89.123.233:3128",
    "145.14.97.190:80",
    "97.153.111.160:8888",
    "147.112.166.40:8081",
    "75.42.103.9:8888",
    "46.40.33.166:8080",
    "123.182.172.175:8888",
    "138.160.183.219:3128",
    "59.10.242.145:3128",
    "217.15.105.194:3128",
    "107.201.75.14:1080",
    "128.54.220.39:8081",
    "2.28.88.171:8080",
    "188.0.162.16:8888",
    "89.76.189.236:1337",
    "134.212.106.61:1080",
    "181.72.217.127:80",
    "94.201.159.33:3128",
    "157.190.218.118:8080",
    "89.230.177.102:3128",
    "128.170.130.187:8888",
    "241.203.57.51:8080",
    "2.116.92.231:1337",
    "134.188.181.156:1337",
    "240.112.3.188:1337",
    "184.83.205.196:1337",
    "59.223.127.198:8081",
    "69.213.55.160:80",
    "117.208.12.244:1080",
    "197.151.109.229:8080",
    "237.130.65.186:1080",
    "163.106.218.251:80",
    "231.138.2.142:80",
    "175.113.202.96:80",
    "138.107.46.92:8081",
    "167.191.161.74:1080",
    "150.173.214.183:8888",
    "232.31.53.139:1337",
    "123.147.127.61:1337",
    "69.245.240.197:1337",
    "20.101.108.63:8080",
    "101.152.200.110:8080",
    "183.225.26.20:3128",
    "53.66.186.194:8888",
    "90.15.55.66:3128",
    "32.143.23.28:8080",
    "173.21.147.97:80",
    "169.218.57.38:1080",
    "159.204.87.107:3128",
    "101.99.22.161:1337",
    "220.133.106.112:8080",
    "93.51.155.135:3128",
    "19.63.102.141:8081",
    "142.145.228.46:8080",
    "167.203.73.164:80",
    "32.227.22.131:80",
    "182.61.205.229:8888",
    "92.232.12.131:8081",
    "114.136.140.15:1080",
    "136.77.173.122:3128",
    "153.36.55.132:1337",
    "31.117.180.231:80",
]

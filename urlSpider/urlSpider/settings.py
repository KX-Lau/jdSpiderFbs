BOT_NAME = 'urlSpider'

SPIDER_MODULES = ['urlSpider.spiders']
NEWSPIDER_MODULE = 'urlSpider.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 64

DOWNLOAD_TIMEOUT = 10  # 下载超时
DOWNLOAD_DELAY = 0.5  # 下载延迟

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

COOKIES_ENABLED = False

REDIRECT_ENABLED = False  # 禁止重定向
RETRY_ENABLED = False  # 禁止重试

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# 开启下载中间件
DOWNLOADER_MIDDLEWARES = {
    'urlSpider.middlewares.UrlspiderDownloaderMiddleware': 543,
}

# 开启管道
ITEM_PIPELINES = {
    # 'urlSpider.pipelines.UrlGoodsIdRedisPipeline': 301,
    # 'urlSpider.pipelines.AllGoodsIdRedisPipeline': 300,
    'urlSpider.pipelines.CommentUrlRedisPipeline': 302,
    # 'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 增加一个去重容器类的配置, 作用是使用redis的set集合来存储请求的指纹数据, 实现请求去重的持久化
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 使用scrapy-redis组件自己的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 配置调度器是否要持久化, 即当爬虫结束时, 要不要清空redis中请求队列和去重指纹的set.
# 如果是True, 表示要持久化存储, 就不会清空数据, 否则清空数据
SCHEDULER_PERSIST = True

# 设置日志等级
LOG_LEVEL = 'ERROR'

# 设置redis
REDIS_HOST = '219.216.65.249'
REDIS_PORT = 6379

GOODS_IDS_KEY = 'all_goods_ids'


# 评论url
COMMENT_URL = 'https://club.jd.com/comment/productPageComments.action?productId=%s&score=0&sortType=5&page=0&pageSize=10&categorys=%s'

USER_AGENT_LIST = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36',
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET4.0C; .NET4.0E; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400',
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
]

IP_LIST = [
    'http://122.224.65.197:3128',
    'http://106.3.45.16:58080',
    'http://222.121.116.26:49480',
    'http://187.44.1.172:8080',
    'http://218.60.8.83:3129',
    'http://58.220.95.86:9401',
    'http://221.122.91.76:9480',
    'http://45.250.226.14:3128',
    'http://216.158.229.67:3128',
    'http://59.36.10.79:3128',
    'http://58.220.95.78:9401',
    'http://177.200.206.167:8080',
    'http://221.122.91.74:9401',
    'http://103.95.40.211:3128',
    'http://58.220.95.79:10000',
    'http://103.78.252.89:8080',
    'http://221.122.91.65:80',
    'http://51.161.116.223:3128',
    'http://58.220.95.80:9401',
    'http://218.60.8.99:3129',
    'http://116.196.85.150:3128',
    'http://221.122.91.34:80',
    'http://183.220.145.3:80',
    'http://220.174.236.211:8091',
    'http://58.220.95.54:9400',
    'https://150.138.253.72:808',
    'http://221.122.91.64:80',
    'http://58.220.95.90:9401',
    'http://182.18.13.149:53281',
    'http://221.122.91.64:9401',
    'http://202.57.2.19:8080',
    'http://103.148.210.110:8080',
    'http://1.10.141.220:54620',
    'http://221.122.91.59:80',

]

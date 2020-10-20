import redis

rs = redis.StrictRedis(host='127.0.0.1', decode_responses=True)

keywords = {
    '电脑': [('戴尔', 'Dell'), ('联想', 'Lenovo')],
    '手机': [('华为', 'HUAWEI'), ('小米', 'MI')],
}

url = 'https://search.jd.com/search?keyword=%s&ev=exbrand_%s（%s）&page=%d'

start_page = 5
end_page = 10

for i in range(2 * start_page - 1, 2 * end_page, 2):
    kw = list(keywords.keys())[0]
    catalog_url = format(url % (kw, keywords[kw][0][0], keywords[kw][0][1], i))
    # print(catalog_url)
    rs.lpush('jdUrl', catalog_url)

# 启动爬虫
# cd F:\python_workspace\JdSpiderFbs\urlSpider\urlSpider\spiders
# scrapy crawl jdurl

# cd F:\python_workspace\JdSpiderFbs\commentSpider\commentSpider\spiders
# scrapy crawl jdcomment

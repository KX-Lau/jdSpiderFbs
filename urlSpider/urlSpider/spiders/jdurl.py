# -*- coding: utf-8 -*-
import redis
from scrapy.utils.project import get_project_settings
from scrapy import Request
from scrapy_redis.spiders import RedisSpider
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ..items import GoodsIdItem
from urllib.parse import unquote

chrome_options = Options()
chrome_options.add_argument('--headless')  # 浏览器不提供可视化界面, 即无头模式
chrome_options.add_argument('--disable-gpu')  # 官方文档建议, 避免bug
chrome_path = r'../utils/chromedriver.exe'  # 指定浏览器位置

category_dict = {
    '电脑': {'戴尔': '0-0', '联想': '0-1'},
    '手机': {'华为': '1-0', '小米': '1-1'},
}


class JdurlSpider(RedisSpider):
    name = 'jdurl'
    redis_key = 'jdUrl'

    def __init__(self):
        super(JdurlSpider, self).__init__()

        # 实例一个浏览器对象
        self.browser = webdriver.Chrome(executable_path=chrome_path, chrome_options=chrome_options)
        self.browser.set_page_load_timeout(10)

        self.settings = get_project_settings()

        self.rs = redis.StrictRedis(host=self.settings['REDIS_HOST'], decode_responses=True)
        self.detail_url = 'https://item.jd.com/%s.html'

    def parse(self, response):

        li_list = response.xpath('//*[@id="J_goodsList"]/ul/li')
        print(response, len(li_list))

        # 商品类别品牌, 在商品评论url中携带
        category = unquote(response.url).split('&')[0][-2:]             # 大类别: 电脑
        brand = unquote(response.url).split('&')[1].split('_')[1][:2]   # 品牌: 联想
        categorys = category_dict[category][brand]                      # 0-1

        if len(li_list) == 60:

            for li in li_list:

                # 爬取到商品id
                url_goods_id = li.xpath('@data-sku').extract_first()

                shop = '无'
                if categorys[0] == '0':             # 电脑
                    shop = li.xpath('./div/div[5]/span/a/text()')
                    shop = shop.extract_first() if shop else '无'
                if categorys[0] == '1':             # 手机
                    shop = li.xpath('./div/div[7]/span/a/text()')
                    shop = shop.extract_first() if shop else '无'

                # 过滤掉官方,自营和二手店家的商品, 且商品id不在相应的集合中
                shop_condition = not ('自营' in shop or '二手' in shop or '官方' in shop)
                id_condition = not (self.rs.sismember(self.settings['GOODS_IDS_KEY'], url_goods_id))
                # print(shop_condition, id_condition)

                if shop_condition and id_condition:
                    # print(url_goods_id, shop)

                    # 商品id+类别, 存储到redis中
                    self.rs.sadd(self.settings['GOODS_IDS_KEY'], url_goods_id)

                    item = GoodsIdItem()
                    item['url_goods_id'] = url_goods_id
                    item['categorys'] = categorys           # 商品评论url携带类别参数
                    yield item

                    # id没有被存储, 发请求, 存同类id
                    yield Request(url=format(self.detail_url % url_goods_id), callback=self.parse_detail,
                                  dont_filter=True)

                else:
                    continue

        else:
            # 每页的商品没有全部加载时, 重新发送请求
            yield Request(url=response.url, callback=self.parse, dont_filter=True)

    def parse_detail(self, response):

        # print(response)

        # categorys = response.meta['categorys']

        color_divs = response.xpath('//*[@id="choose-attr-1"]/div[2]/div')
        ver_divs = response.xpath('//*[@id="choose-attr-2"]/div[2]/div')
        color_divs.extend(ver_divs)
        # print('div_list--->: ', color_divs)

        for div in color_divs:
            all_goods_id = div.xpath('@data-sku').extract_first()
            # print(all_goods_id)

            self.rs.sadd(self.settings['GOODS_IDS_KEY'], all_goods_id)

    def closed(self, spider):
        self.browser.quit()

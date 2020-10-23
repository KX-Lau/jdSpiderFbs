# -*- coding: utf-8 -*-
from scrapy.http import Request
import json
from scrapy_redis.spiders import RedisSpider
from urllib.parse import urlparse, parse_qs
from ..items import CommentspiderItem
import redis
from scrapy.utils.project import get_project_settings


class JdcommentSpider(RedisSpider):
    name = 'jdcomment'

    redis_key = 'jdComment'

    def __init__(self):
        super(JdcommentSpider, self).__init__()
        self.settings = get_project_settings()
        self.rs = redis.StrictRedis(host=self.settings['REDIS_HOST'], decode_responses=True)

    def parse(self, response):
        """解析商品评论---首页"""

        if response.text:
            comment_info = json.loads(response.text)
            print(response)

            # 评论最大页数
            max_page = comment_info['maxPage']
            # 从url中获取到商品id, 和商品类别品牌
            goods_id = parse_qs(urlparse(response.url).query)['productId'][0]
            categorys = parse_qs(urlparse(response.url).query)['categorys'][0]

            # 评论列表
            comment_list = comment_info['comments']
            if not comment_list:
                # print('评论列表为空!!!')
                return

            for comment in comment_list:
                item = CommentspiderItem()
                item['user_id'] = comment['id']
                item['user_name'] = comment['nickname']
                item['goods_id'] = goods_id
                item['score'] = comment['score']
                item['creat_time'] = comment['creationTime']
                item['content'] = comment['content'].replace('\n', ' ')
                item['categorys'] = categorys

                yield item

            # 爬取评论第2页到最后一页
            for page in range(1, max_page):
                yield Request(url=format(self.settings['COMMENT_URL'] % (goods_id, page, categorys)),
                              callback=self.parse_next)

    def parse_next(self, response):
        """解析商品评论---除首页"""

        if response.text:
            comment_info = json.loads(response.text)
            print('url', response.url)

            item = CommentspiderItem()
            # 从url中获取到商品id
            item['goods_id'] = parse_qs(urlparse(response.url).query)['productId'][0]
            item['categorys'] = parse_qs(urlparse(response.url).query)['categorys'][0]

            # 评论列表
            comment_list = comment_info['comments']
            if not comment_list:
                # print('评论列表为空!!!')
                return

            for comment in comment_list:
                item['user_id'] = comment['id']
                item['user_name'] = comment['nickname']
                item['score'] = comment['score']
                item['creat_time'] = comment['creationTime']
                item['content'] = comment['content'].replace('\n', ' ')

                yield item

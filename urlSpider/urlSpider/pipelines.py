import redis
from scrapy.utils.project import get_project_settings


# class UrlGoodsIdRedisPipeline(object):
#
#     def process_item(self, item, spider):
#         rs.sadd(settings['COMMENTS_URL_KEY'], item['url_goods_id'])
#
#         return item


# class AllGoodsIdRedisPipeline(object):
#
#     def process_item(self, item, spider):
#         rs.sadd(settings['ALL_GOODS_KEY'], item['all_goods_id'])
#
#         return item


class CommentUrlRedisPipeline(object):
    def __init__(self):
        self.settings = get_project_settings()
        self.rs = redis.StrictRedis(host=self.settings['REDIS_HOST'], decode_responses=True)

    def process_item(self, item, spider):
        self.rs.lpush('jdComment', format(self.settings['COMMENT_URL'] % (item['url_goods_id'], item['categorys'])))

        return item

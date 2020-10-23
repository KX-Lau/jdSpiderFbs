from scrapy.utils.project import get_project_settings
import csv
import redis
import json


class CommentCsvPipeline(object):

    def __init__(self):
        self.settings = get_project_settings()
        self.comment_fp = None
        self.comment_writer = None

    def open_spider(self, spider):
        print('开始爬取商品评论内容.................')
        self.comment_fp = open('../comments_info51-60.csv', 'w', newline='', encoding='utf-8')
        self.comment_writer = csv.DictWriter(self.comment_fp, fieldnames=self.settings['COMMENT_COL'])
        self.comment_writer.writeheader()

    def process_item(self, item, spider):
        self.comment_writer.writerow(item)
        return item

    def close_spider(self, spider):
        self.comment_fp.close()
        print('爬取商品评论内容结束.................')


class CommentRedisPipeline(object):
    def __init__(self):
        self.rs = redis.StrictRedis(host='219.216.65.249', decode_responses=True)
        self.key = 'comments'

    def process_item(self, item, spider):

        item_dict = dict(item)
        self.rs.sadd(self.key, json.dumps(item_dict, ensure_ascii=False))
        return item





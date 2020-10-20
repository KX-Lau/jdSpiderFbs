from scrapy import signals
import random
from twisted.internet.error import TimeoutError, ConnectionRefusedError, ConnectionLost


class CommentspiderDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):

        # UA伪装
        request.headers['User-Agent'] = random.choice(spider.settings['USER_AGENT_LIST'])
        # print(request.headers['User-Agent'])

        request.meta['proxy'] = random.choice(spider.settings['IP_LIST'])
        # request.meta['proxy'] = linecache.getline(spider.settings['PROXY_FILE'], random.randint(1, 200))

        # 返会None, 表示继续处理该请求
        return None

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):

        if isinstance(exception, (TimeoutError, ConnectionRefusedError, ConnectionLost)):
            return request
        else:
            print('发生异常的请求>>>>>>>>>>>>>', request, request.meta['proxy'], exception)
            return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

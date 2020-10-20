from scrapy import signals
import time
import random
from scrapy.http import HtmlResponse
from twisted.internet.error import TimeoutError, ConnectionRefusedError, ConnectionLost


class UrlspiderDownloaderMiddleware(object):

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):

        # UA伪装
        request.headers['User-Agent'] = random.choice(spider.settings['USER_AGENT_LIST'])

        request.meta['proxy'] = random.choice(spider.settings['IP_LIST'])
        # print(request.meta['proxy'])

        # 返会None, 表示继续处理该请求
        return None

    def process_response(self, request, response, spider):

        if request.url.startswith('https://search.jd.com/search?keyword'):

            # 拿到浏览器对象
            browser = spider.browser
            browser.get(request.url)
            # 执行下滑到底部的操作
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            # 休眠, 等待获取完全信息
            time.sleep(5)

            # 包含动态加载后30条的数据
            page_text = browser.page_source
            new_response = HtmlResponse(url=request.url, body=page_text, encoding='utf-8', request=request)
            return new_response

        else:
            return response

    def process_exception(self, request, exception, spider):

        if isinstance(exception, (TimeoutError, ConnectionRefusedError, ConnectionLost)):
            return request
        else:
            print('发生异常的请求>>>>>>>>>>>>>', request, request.meta['proxy'], exception)
            return request

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

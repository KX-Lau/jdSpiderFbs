import scrapy


class GoodsIdItem(scrapy.Item):

    url_goods_id = scrapy.Field()       # 构造评论url的商品id,
    # all_goods_id = scrapy.Field()       # 同类url, 评论相同


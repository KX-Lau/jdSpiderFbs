import scrapy


class GoodsIdItem(scrapy.Item):

    url_goods_id = scrapy.Field()       # 构造评论url的商品id,
    categorys = scrapy.Field()          # 商品类别,



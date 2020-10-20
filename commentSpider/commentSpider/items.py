import scrapy


class CommentspiderItem(scrapy.Item):
    user_id = scrapy.Field()  # 用户id
    user_name = scrapy.Field()  # 用户昵称
    goods_id = scrapy.Field()  # 商品id
    score = scrapy.Field()  # 评分
    creat_time = scrapy.Field()  # 评论时间
    content = scrapy.Field()  # 评论内容

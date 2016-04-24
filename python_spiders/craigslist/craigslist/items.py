import scrapy


class CraigsListItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
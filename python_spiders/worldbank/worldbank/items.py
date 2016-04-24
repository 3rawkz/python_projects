import scrapy


class WorldBankItem(scrapy.Item):
    COUNTRY = scrapy.Field()
    PERCAPITAGDP2014 = scrapy.Field()
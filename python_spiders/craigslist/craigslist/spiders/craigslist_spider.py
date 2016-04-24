import scrapy
from craigslist.items import CraigsListItem


class CraigsListSpider(scrapy.Spider):
    name = "craigslist"
    allowed_domains = ["craigslist.org"]
    start_urls = [
        "https://akroncanton.craigslist.org/search/w4w"
    ]

    def parse(self, response):
        # why does the beginning of the path need 2 '//' for xpath arguments?
        for sel in response.xpath('//a[@class = "hdrlnk"]'):
            item = CraigsListItem()
            # appends with the '/' - no need to lead with one in the argument
            item['title'] = sel.xpath('span[@id="titletextonly"]/text()').extract()
            item['link'] = sel.xpath('@href').extract()
            yield item


class CraigsListM4WSpider(scrapy.Spider):
    name = "clM4W"
    allowed_domains = ["craigslist.org"]
    paginator = ['', '200', '300', '400', '500', '600']
    start_urls = [
        "https://akroncanton.craigslist.org/search/m4w/%s" % page for page in paginator
        ]

    def parse(self, response):
        for sel in response.xpath('//a[@class = "hdrlnk"]'):
            item = CraigsListItem()
            item['title'] = sel.xpath('span[@id="titletextonly"]/text()').extract()
            item['link'] = sel.xpath('@href').extract()
            yield item

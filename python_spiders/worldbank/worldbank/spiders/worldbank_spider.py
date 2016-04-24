import scrapy
from worldbank.items import WorldBankItem
from worldbank.scrubbers import is_num, clean_data


class WorldBankSpider(scrapy.Spider):
    name = 'worldbank'
    allowed_domains = 'worldbank.org'
    start_urls = ['http://data.worldbank.org/indicator/NY.GDP.PCAP.CD']

    # parse only gets called once so it's appropriate to use an iterable and a generator
    def parse(self, response):
            for selection in response.xpath('//div[@ class ="view-content"]//tr'):
                item = WorldBankItem()
                item['COUNTRY'] = selection.xpath('td[@ class="views-field views-field'
                                                  '-country-value"]/a/text()').extract()
                item['PERCAPITAGDP2014'] = clean_data(selection.xpath('td[@ class="views-field views-field-wbapi-data-'
                                                                'value-2014 wbapi-data-value wbapi-data-value-last"]'
                                                                '/text()').extract())
                yield item  # generator outputs a copy of the derived values without storing them

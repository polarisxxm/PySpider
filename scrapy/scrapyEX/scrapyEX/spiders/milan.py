# coding: utf-8
# first spider called [milan]

import scrapy
from scrapyEX.items import ScrapyexItem


class MiLan(scrapy.Spider):
    name = "milan"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # filename = response.url.split('/')[-2] + '.html'  # Books.html/Resources.html
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        for sel in response.xpath('//ul/li'):
            # xpath: a/text(), a/@href text()
            sitem = ScrapyexItem()
            sitem['title'] = sel.xpath('a/text()').extract()
            sitem['link'] = sel.xpath('a/@href').extract()
            sitem['desc'] = sel.xpath('text()').extract()
            yield sitem


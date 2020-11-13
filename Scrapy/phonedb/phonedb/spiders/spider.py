import scrapy
from pprint import pprint


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['phonedb.net']
    start_urls = ['http://phonedb.net/index.php?m=device&s=list&first=apple']

    def parse(self, response):
        for row in response.css("div:nth-child(7)"):

            yield {
                "phone_title": row.css(f"div.content_block_title > a::text").extract_first(),
                "phone_link": row.css(f"div.content_block_title > a::attr(href)").extract_first()
            }

    def start_requests(self):
        url = "http://phonedb.net/index.php?m=device&s=list&first=apple"
        yield scrapy.Request(url=url, callback=self.parse)

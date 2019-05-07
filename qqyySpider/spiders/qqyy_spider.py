# -*- coding: utf-8 -*-
import scrapy


class QqyySpiderSpider(scrapy.Spider):
    name = 'qqyy_spider'
    allowed_domains = ['y.qq.com']
    start_urls = ['https://y.qq.com/n/yqq/song/002eTq6539AsfN.html']

    def parse(self, response):
        # filename = 'qq-music.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)


        self.logger.info('current crawl url:%s' % response.url)
        self.logger.info(response.css('title::text').extract_first())
        self.logger.info(response.xpath("//li[contains(@class,'js_company')]/@class").extract_first())

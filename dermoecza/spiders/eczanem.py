# -*- coding: utf-8 -*-

import scrapy

from ..items import DermoeczaItem


class EczanemSpider(scrapy.Spider):
    name = 'eczanem'
    allowed_domains = ['www.dermoeczanem.com']
    start_urls = ['https://www.dermoeczanem.com/mineral-gunes-urunleri']

    def parse(self, response):

        for href in response.css("div.productItem"):
            url = response.urljoin(href.css('a::attr(href)').extract_first())
            yield scrapy.Request(url, callback=self.parse_item)

    def parse_item(self, response):

        item = DermoeczaItem()

        name = response.css("h1.chbarcodename::text").extract_first()
        barcode = response.css("span.chbarcode::text").extract_first()
        brand = response.css("a.productBrand::text").extract_first()
        image = response.css("a.image-wrapper::attr(href)").extract_first()
        url = response.css("head link::attr(href)").extract_first()

        item['name'] = name
        item['barcode'] = barcode
        item['brand'] = brand
        item['image'] = image
        item['url'] = url
        return item

# -*- coding: utf-8 -*-
import scrapy


class LinkedinSpider(scrapy.Spider):
    name = "linkedin"
    allowed_domains = ["ru.linkedin.com"]
    start_urls = (
        'http://www.ru.linkedin.com/',
    )

    def parse(self, response):
        pass

# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#creating my item containers
class FundrazItem(scrapy.Item):
    title = scrapy.Field()
    target = scrapy.Field()
    amountraised = scrapy.Field()
    numbercontributors = scrapy.Field()
    currencyused = scrapy.Field()
    startDate = scrapy.Field()
    category = scrapy.Field()
        



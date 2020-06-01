# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AssignmentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    quotes = scrapy.Field()
    authors = scrapy.Field()
    prices = scrapy.Field()
    ratings = scrapy.Field()
    pass

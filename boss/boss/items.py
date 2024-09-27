# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BossItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job_name = scrapy.Field()
    job_salary = scrapy.Field()
    experience = scrapy.Field()
    degree = scrapy.Field()
    company_name = scrapy.Field()
    city = scrapy.Field()
    area = scrapy.Field()
    job_skills = scrapy.Field()
    

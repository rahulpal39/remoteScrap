# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

import pathlib


class QuotesItem(scrapy.Item):
    author = scrapy.Field()
    text = scrapy.Field()


class JobItem(scrapy.Item):
    company_logo=scrapy.Field()
    job_title=scrapy.Field()
    company_name=scrapy.Field()
    company_email=scrapy.Field()
    is_approved=scrapy.Field()
    is_active=scrapy.Field()
    is_filled=scrapy.Field()
    is_featured=scrapy.Field()
    company_url=scrapy.Field()
    job_country=scrapy.Field()
    job_state=scrapy.Field()
    job_zip_code=scrapy.Field()
    job_city=scrapy.Field()
    job_address=scrapy.Field()
    category=scrapy.Field()
    type=scrapy.Field()
    payment_method=scrapy.Field()
    job_created_at=scrapy.Field()
    job_expires_at=scrapy.Field()
    company_website=scrapy.Field()
    job_description=scrapy.Field()
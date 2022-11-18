import json
from urllib.parse import quote_plus
import scrapy
from ..items import JobItem, QuotesItem

import urllib.parse
from urllib.parse import urljoin, urlparse

# Python3 program to check
# URL is valid or not
# using regular expression
import re

# Function to validate URL
# using regular expression


def isValidURL(str):

    # Regex to check valid URL
    regex = ("((http|https)://)(www.)?" +
             "[a-zA-Z0-9@:%._\\+~#?&//=]" +
             "{2,256}\\.[a-z]" +
             "{2,6}\\b([-a-zA-Z0-9@:%" +
             "._\\+~#?&//=]*)")

    # Compile the ReGex
    p = re.compile(regex)

    # If the string is empty
    # return false
    if (str == None):
        return False

    # Return if the string
    # matched the ReGex
    if (re.search(p, str)):
        return True
    else:
        return False

    # Driver code


# This code is contributed by avanitrachhadiya2155


class QuotesSpider(scrapy.Spider):

    start_urls = [
        'https://www.moxa.com/en/products/']

    name = "product"

    allowed_domains = ['moxa.com']
    # start_urls = ['http://books.toscrape.com/']
    base_url = 'https://www.moxa.com'

    def parse(self, response, **kwargs):
        # item = JobItem()
        import json

        all_div_quotes = response.css('div.container')
        for quote in all_div_quotes.css('div.alphabet-lists'):
            json_object = quote.extract()
            url = quote.css('a::attr(href)').extract()
            urlJob = url
            for ur in url:
                # print(ur)

                book_url = self.base_url + ur
                # book_url = 'https://www.moxa.com/en/products/industrial-edge-connectivity/controllers-and-ios/rugged-controllers-and-i-os/iologik-e1500-series'
                print(book_url)
                yield scrapy.Request(book_url, callback=self.parse_book)

    def parse_book(self, response):
        print(response)
    #     item = JobItem()
        import json

    #     #header work post
        JobData = response.css('div.body-section')
        prouctD = response.css("div.container")
        prouctFeature = response.css("span.i-list__text::text").extract()

        pTitle = prouctD.css('h2.hero-banner__heading::text').extract()
        pheading = prouctD.css('h3.hero-banner__subheading::text').extract()
        prouctimage = response.css("div.showcase-block__detail")
        Imageurl = prouctimage.css('img').xpath('@src').extract()
#################################################overview##################################
        overview = prouctD.css('div.side-section__main')
        overtitile = overview.css("h3.module-block__heading::text").extract()
        # overdetail=overview.css("h3.module-block__heading::text").extract()
        overperagraph = overview.css(
            "p.module-block__paragraph::text").extract()
        oversubhedding = overview.css(
            "h4.module-block__subheading::text").extract()
#################################################specifications##################################
        specifications = prouctD.css('div.side-section__main')
        specifTitle = specifications.css(
            'h3.basic-accordion__heading::text').extract()
        specifsubH3 = specifications.css(
            'h4.title-list__heading::text').extract()
        specifsubparaG = specifications.css(
            'p.title-list__paragraph::text').extract()
        print(overtitile, specifsubparaG)

        # for para in overperagraph:
        #     print(para)
        over={}

            

        for spHubH3 in specifsubH3:
            print(spHubH3)
        for Title in specifTitle:
            print(Title)

        dictionary = {
            'vendor': "MOXA",
            'Product': pTitle,
            # 'Feature':,
            'series': {
                'Name': pTitle,
                'Title': pheading,
                'Features and Benefits': prouctFeature,
            },
            'Overview': {
                # overtitile[0]:overperagraph,
                
                # overdetail: overperagraph,
                # oversubhedding: overperagraph,


            },
            "Specifications": {
                # specifTitle
                # : {
                #     # spHubH3: specifsubparaG

                # }


            },


        }
        name=f"{pTitle}.json"

        with open(name, "w") as outfile:
            json.dump(dictionary, outfile)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

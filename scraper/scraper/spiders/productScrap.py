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


def log(data, name=None):
    PrettyJson = json.dumps(
        data, indent=4, separators=(',', ': '), sort_keys=True)

    print(
        '#################################################{name}##################################')
    print(PrettyJson)
    return PrettyJson
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

                # book_url = self.base_url + ur
                book_url = 'https://www.moxa.com/en/products/industrial-edge-connectivity/controllers-and-ios/rugged-controllers-and-i-os/iologik-e1500-series'
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
        print(oversubhedding)
        print(overperagraph)
        

        
#################################################specifications##################################
        specifications = prouctD.css('div.side-section__main')
        # specifTitle = specifications.css(
        #     '.basic-accordion__heading::text').extract()
        # specifsubH3 = specifications.css(
        #     '.title-list__heading::text').extract()
        # specifsubparaG = specifications.css(
        #     'p.title-list__paragraph::text').extract()
        # # print(overtitile, specifsubparaG)

        # specifdat = specifications.css(
        #     'div.basic-accordion__block').extract()
        # print(json.dump(specifdat))
        # json.dump(student, write_file, indent=4)
        # res=log(specifsubH3,'demo')
        spec = []
        dates_dict = dict()
        num_list=[] 
        # dict = dict() 

        num_listparagrap=[]
        num_listspTitls=[]
        property_data = {}

        for para in specifications.css('.basic-accordion__block'):
            # print(para.css(".basic-accordion__heading::text").extract())
            # print(para)
            sptitile = para.css(".basic-accordion__heading::text").extract()

            # print(sptitile[0])
            d=sptitile[0]
            # dict
            spec.append(sptitile[0])
            
          

            for pa  in para.css('.title-list'):
                paragrap = pa.css(".title-list__paragraph::text").extract()
                pTitls = pa.css(".title-list__heading::text").extract()
                data = {}
                num_listparagrap.append(paragrap)
                num_listspTitls.append(pTitls)
                dic=[]

                for pare in pTitls: 
                    for itit in paragrap:       
                        dic.append(itit) 
                    for i in dic:
                                        
                        data[pare]=i
                        property_data[d]=data

                # print(pa.css(".title-list__heading::text").extract())
                # print(pa.css(".title-list__paragraph::text").extract())
                # spec.append(sptitile[0])
                # # data={
                # d[sptitile].append(pTitls)
                # print(key) 


        
            # print(property_data)
        # tle=pTitle[0]
        # pT=pTitle[0]
        # phe=pheading[0]
        # dictionary = {
        #     'vendor': "MOXA",
        #     'Product':tle ,
        #     # 'Feature':,
        #     'series': {
        #         'Name': pT,
        #         'Title': phe,
        #         'Features and Benefits': prouctFeature,
        #     },
        #     'Overview': {
        #         'overtitile':'demo',

        #         # overdetail: overperagraph,
        #         # oversubhedding: overperagraph,

        #     },
        #     "speacification":property_data,

          

        # }
        # # name=f"{tle}.json"
        # # print(dictionary)
        # # with open(name, "w") as outfile:
        # #     json.dump(dictionary, outfile)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

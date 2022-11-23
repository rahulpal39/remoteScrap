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
        pageData = response.css('.tab-section__main')

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
            ".module-block__paragraph::text").extract()
        oversubhedding = overview.css(
            ".module-block__subheading::text").extract()
        # print(oversubhedding)
        # print(overperagraph)
        datas = {}
        datas['introducation'] = overperagraph

#################################################specifications##################################
        specifications = prouctD.css('div.side-section__main')     
        spec = []
        dates_dict = dict()
        num_list = []
        num_listparagrap = []
        num_listspTitls = []
        property_data = {}

        for para in specifications.css('.basic-accordion__block'):
            # print(para.css(".basic-accordion__heading::text").extract())
            # print(para)
            sptitile = para.css(".basic-accordion__heading::text").extract()

            # print(sptitile[0])
            d = sptitile[0]
            # dict
            spec.append(sptitile[0])

            for pa in para.css('.title-list'):
                paragrap = pa.css(".title-list__paragraph::text").extract()
                pTitls = pa.css(".title-list__heading::text").extract()
                data = {}
                num_listparagrap.append(paragrap)
                num_listspTitls.append(pTitls)
                dic = []

                for pare in pTitls:
                    for itit in paragrap:
                        dic.append(itit)
                    for i in dic:

                        data[pare] = i
                        property_data[d] = data
               
        #################################resource###############################################

        dataaa = pageData.css('.bold-title-heading::text').extract()
        rheading = dataaa[0]
        # filename = []
        tableHeading = pageData.css(".border-table__th::text").extract()
        filename = pageData.css(".js-checksum-filename::text").extract()
        filetype = pageData.css(".js-checksum-type::text").extract()
        filechecksum = pageData.css(
            ".border-table__checksum__text::text").extract()
        fileLink = pageData.css(".border-table__link")
        apply_url = fileLink.css('a::attr(href)').extract()  # apply link grap

        fileData = pageData.css(".border-table__dash-list")
        osList = []
        for fin in fileData:
            fileLinks = fin.css(".border-table__list::text").extract()
            osList.append(fileLinks)
        datalunch = pageData.css(
            '.date-short::text').extract()  # apply link grap

        # print(osList)
        # print(datalunch)
        print(len(filename))
        # print(filen)

        # {
        #     "NAME": "Firmware for VPort 06EC-2V Series",
        #     "size": "43.4 MB",
        #     "TYPE": "Firmware",
        #     "Details":  {
        #         "File Name": "Firmware for VPort 06EC-2V Series",
        #         "Version": "v1.2",
        #         "SHA-512 Checksum": "aa16fb972f0ed12ecaf78341509c4574c55aaf7d38b9f43f2dd89cca0418aa228b55c1ba4b03eb4dd732b21a9857a7083074a05a83e9ef61d3eede3a49eb48d6"
        #     },
        #     "VERSION": "v1.2",
        #     "OPERATING SYSTEM": "-",
        #     "RELEASE DATE": "Dec 03, 2021",
        #     "Release notes": "https://cdn-cms.azureedge.net/Moxa/media/PDIM/S100000358/VPort%2006EC-2V%20Series_moxa-vport-06ec-2v-series-firmware-v1.2.rom_Software%20Release%20History.pdf"
        # },
       
        filenam=filename
        l = []

        i = 0
        import string
        
        while i < len(filename):

            resdata={}  
            resdata['NAME']=filename[i].replace("\r\n","") 
            resdata['TYPE']=filetype[i].replace("\r\n","") 
            resdata['Details']=filechecksum[i].replace("\r\n","") 
            resdata['Release notes']=apply_url[i].replace("\r\n","") 
            resdata['OPERATING SYSTEM']=osList[i]
            resdata['RELEASE DATE']=datalunch[i].replace("\r\n","") 

            # print(resdata)
            # print(filename[i])
            # print(apply_url[i])
                # print(filechecksum[i])
                # print(fileDatalist[i])
                # print(osList[i])
                # print(datalunch[i])
            l.append(resdata)
            i += 1

        # print(l)
        # model-table"

        #############################Models#################################
        # d=pageData.css('.model-table').extract():
        models= pageData.css(".model-table")
        model_Text = models.css('a::text').extract()#apply link grap
        modelImage=models.css('.model-table__img::attr(src)').extract()
        # modelImage = companyLogo.css('img').xpath('@src').extract()
        modelTD=models.css('td::text').extract()
        # print(modelTD)
        # print(model_url)

        # resdata={}  
        # resdata['NAME']=filename[i].replace("\r\n","") 
        reslist={}
            
        reslist['models']=model_Text
        reslist['modelImageUrl']=modelImage
        reslist['compare']=modelTD



        # print(resdata)
        # for a in pageData.css(".js-checksum-filename::text").extract():
        #             # print(a)
        #             tableHeading.append(a)
        # border-table
        #     # print(property_data)
        # print(reslist)
        tle=pTitle[0]
        pT=pTitle[0]
        phe=pheading[0]
        dictionary = {
            'vendor': "MOXA",
            'Product':tle ,
            # 'Feature':,
            'series': {
                'Name': pT,
                'Title': phe,
                'Features and Benefits': prouctFeature,
            },
            'Overview': {
                'overtitile':datas,

            },
            "speacification":property_data,
            'Resources':reslist,

        }
        name=f"{tle}.json"
        # print(dictionary)
        with open(name, "w") as outfile:
            json.dump(dictionary, outfile,ensure_ascii=False, indent=4)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

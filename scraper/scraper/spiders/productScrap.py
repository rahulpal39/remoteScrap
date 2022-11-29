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

                book_url = self.base_url + ur
                # book_url = 'https://www.moxa.com/en/products/industrial-network-infrastructure/secure-routers/secure-routers/edr-810-series'
                print(book_url)
                yield scrapy.Request(book_url, callback=self.parse_book)

    def parse_book(self, response):
        # print(response)
    #     item = JobItem()
        import json

    #     #header work post
        model=response.css('.modal__body')
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
                # print(len(pTitls))
                num_listparagrap.append(paragrap)
                num_listspTitls.append(pTitls)
                dic = []
                i = 0
                while i < len(pTitls):
                    # print(pTitls[i],paragrap[i])
                    data[pTitls[i]] = paragrap[i]
                    property_data[d] = data
                    
                    

                    i += 1
                    # if i == 3:
                    #     continue
                    # print(i)

                # for pare in pTitls:
                #     for itit in paragrap:
                #         dic.append(itit)

                #         data[pare] = itit
                #         property_data[d] = data
               
        #################################resource###############################################

        dataaa = pageData.css('.bold-title-heading::text').extract()
        # rheading = dataaa[0]
        # filename = []
        tableHeading = pageData.css(".border-table__th::text").extract()
        filename = pageData.css(".js-checksum-filename::text").extract()
        filetype = pageData.css(".js-checksum-type::text").extract()
        size=pageData.css(".border-table__note::text").extract()
        filechecksum = pageData.css(
            ".border-table__checksum__text::text").extract()
        fileDataSha = model.css(
            "span::text").extract()
        fileLink = pageData.css(".border-table__link")
        apply_url = fileLink.css('a::attr(href)').extract()  # apply link grap
        # 
        durl=pageData.css('.border-table__link record-download')

        download_url = durl.css('a::attr(href)').extract()  # apply link grap

        fileData = pageData.css(".border-table__dash-list")
        osList = []
        for fin in fileData:
            fileLinks = fin.css(".border-table__list::text").extract()
            osList.append(fileLinks)
        datalunch = pageData.css(
            '.date-short::text').extract()  # apply link grap
        # print(osList)
        version= pageData.css(
            ".version-short::text").extract()
       
       
        filenam=filename
        l = []

        i = 0
        import string
        
        while i < len(filename):

            resdata={}  
            resdata['NAME']=filename[i].replace("\r\n","") 
            resdata['Size']=size[i].replace("\r\n","")      
            resdata['Details']={
                "File Name":filename[i].replace("\r\n","") ,
                'Version':version[i].replace("\r\n","") ,
                
            }            
       
            resdata['TYPE']=filetype[i].replace("\r\n","") 
            # resdata['Details']=filechecksum[i].replace("\r\n","") 
            resdata['Release notes']=apply_url[i].replace("\r\n","") 
            resdata['OPERATING SYSTEM']=osList[i]
            resdata['VERSION']=version[i].replace("\r\n","") 
            resdata['RELEASE DATE']=datalunch[i].replace("\r\n","") 
            # download_url

            # print(resdata)
            # print(filename[i])
            # print(apply_url[i])
                # print(filechecksum[i])
                # print(fileDatalist[i])
                # print(osList[i])
                # print(datalunch[i])
            l.append(resdata)
            i += 1

       
        #############################Models#################################
        # d=pageData.css('.model-table').extract():
        com=[]
        models= pageData.css(".model-table")
        for da in models.css("tr"):
            modelsTitle = da.css('td::text').extract()
            # print(modelsTitle)
            com.append(modelsTitle)
       
            
            
        model_Text = models.css('a::text').extract()#apply link grap
        modelImage=models.css('.model-table__img::attr(src)').extract()
        # modelImage = companyLogo.css('img').xpath('@src').extract()
        
        # print(modelTD)
        # print(model_url)

        # resdata={}  
        # resdata['NAME']=filename[i].replace("\r\n","") 
            
        # reslist['models']=model_Text
        # reslist['modelImageUrl']=modelImage
        # reslist['compare']=modelTD
        # print(modelTD)
        md=[]
        
        i = 0
        while i < len(model_Text):
            reslist={}
            
            reslist["Name"]=model_Text[i]
            reslist["link"]=modelImage[i]
            for  ms in com:
                
                if len(ms) >0: 
                    c =i+1                      
                    b = 0
                    reslist[ms[0]]=ms[c ]
            
            md.append(reslist)

            i += 1
        

        # print(md)

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
            'url':response.url,
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
            'Resources':l,
            "Models":md,

        }
        name=f"{tle}.json"
        # print(dictionary)
        with open(name, "w") as outfile:
            json.dump(dictionary, outfile,ensure_ascii=False, indent=4)

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

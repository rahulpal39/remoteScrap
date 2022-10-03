from urllib.parse import quote_plus
import scrapy
from ..items import JobItem, QuotesItem


class QuotesSpider(scrapy.Spider):

    start_urls = [
        'https://weworkremotely.com/categories/remote-front-end-programming-jobs']

    name = "quotes"

    allowed_domains = ['weworkremotely.com']
    # start_urls = ['http://books.toscrape.com/']
    base_url = 'https://weworkremotely.com'

    def parse(self, response, **kwargs):
        item = JobItem()
        import json

        all_div_quotes = response.css('section.jobs')
        for quote in all_div_quotes.css('li.feature'):
            json_object = quote.extract()
            # print(json.dumps(json_object, indent=3))
            url = quote.css('a::attr(href)').extract()
            # print(f"/company/audienceplus'{url[0]}")
            # print(f"remote-jobs,{url[1]}")
            urlJob = url[1]

            book_url = self.base_url + urlJob
            # print(book_url)
            yield scrapy.Request(book_url, callback=self.parse_book)

    def parse_book(self, response):
        # print(response)
        item = JobItem()

        item = JobItem()
        JobData = response.css('div.listing-header-container')
        job_title = JobData.css('h1::text').extract()
        companyLogo = response.css("div.listing-logo")
        companyLog = companyLogo.css('img').xpath('@src').extract()
        content = response.css('div.listing-container').extract()
        aurl = response.css('div.apply_tooltip')
        appl_url = aurl.css('a::attr(href)').extract()
        post_tag=response.css('span.listing-tag::text').extract()
        company = response.css("div.company-card")
        companyCountry = company.css('h3::text').extract()
        company_website = company.css('a::attr(href)').extract()
        company_name = company.css('a::text').extract()

        # print(company_website[2])
        print(companyCountry)
        # print(post_tag[1])

        # print(content)

        # print(url.extract())

        # print(url[1].extract())
        # title = response.xpath('//div/h1/text()').extract_first()

        # for book in all_div_quotes.css('li.feature'):
        # book_url = self.start_urls[0] + \
        #     book.xpath('.//h3/a/@href').extract_first()
        # yield scrapy.Request(book_url, callback=self.parse_book)
        # url = quote.css('a::attr(href)')
        # print(url[1].extract())

        # # replace(
        # #     '”', '').replace("“", "")
        # author = quote.css('li.feature::text').extract_first()

        item['job_title'] = job_title[0]
        item['job_description'] = content[0]
        item['company_logo'] = companyLog[0]
        item['company_website'] = appl_url[0]
        item['company_name']=company_name[0]
        item['company_email']=company_website[2]
        item['company_url']=company_website[2]
        item['job_country']=companyCountry[-1]
        item['job_state']=companyCountry[0]
        item['job_city']=companyCountry[0]
        item['job_address']=companyCountry[0]
        item['category']=post_tag[1]
        item['type']=post_tag[1]
        # # item['payment_method']="cash"
        # # item['job_created_at']=
        # # item['job_expires_at']=

        yield item


        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

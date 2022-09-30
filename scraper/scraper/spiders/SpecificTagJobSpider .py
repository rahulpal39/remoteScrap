import scrapy
from ..items import JobItem, QuotesItem

"""
command: scrapy crawl some-quotes -a author="<author_name>" -L WARN

Example: scrapy crawl some-quotes -a author="Albert Einstein" -L WARN

Those author name should match the name on the site.
"""


class SpecificAuthorQuotesSpider(scrapy.Spider):
    """Extracts the quotes from specific author"""

    name = "jobtag"

    def __init__(self, author=None, **kwargs):
        self.author = author
        self.start_urls = [
            f'https://weworkremotely.com/remote-jobs/search?term={author}&button=']

        super().__init__(**kwargs)

    # url = f'https://weworkremotely.com/remote-jobs/search?term=&button='
    # start_urls = [url]

    allowed_domains = ['weworkremotely.com']
    # start_urls = ['http://books.toscrape.com/']
    base_url = 'https: // weworkremotely.com'

    def parse(self, response, **kwargs):

        item = JobItem()
        import json

        all_div_quotes = response.css('section.jobs')
        for quote in all_div_quotes.css('li.feature'):
            json_object = quote.extract()
            print(json.dumps(json_object, indent=3))
            url = quote.css('a::attr(href)').extract()
            # print(f"/company/audienceplus'{url[0]}")
            # print(f"remote-jobs,{url[1]}")
            urlJob = url[1]

            book_url = self.base_url + urlJob
            spaceUrl = book_url.replace(" ", "")

            yield scrapy.Request(spaceUrl, callback=self.parse_book)

    def parse_book(self, response):
        # print(response)
        item = JobItem()

        JobData = response.css('div.listing-header-container')
        job_title = JobData.css('h1::text').extract()

        companyLogo = response.css("div.listing-logo")
        companyLog = companyLogo.css('img').xpath('@src').extract()

        content = response.css('div.listing-container').extract()
        aurl = response.css('div.apply_tooltip')
        appl_url = aurl.css('a::attr(href)').extract()
        # print(appl_url[0])

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

        item['title'] = job_title[0]
        item['text'] = content[0]
        item['image'] = companyLog[0]
        item['applylink'] = appl_url[0]

        yield item

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)

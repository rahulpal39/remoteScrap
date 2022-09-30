# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from quotes.models import Quotes
from jobs.models import Jobs

import logging
import coloredlogs
logger = logging.getLogger(__name__)
coloredlogs.install(level="WARN", logger=logger)


class ScraperPipeline:

    def process_item(self, item, spider):
        try:
            Quotes.objects.create(text=item['text'], author=item['author'])
            print("\n")
            logger.warn("Loaded quote {}".format(item['text']))
            print(item)
        except Exception as e:
            print("\n")
            logger.error(
                "\nFailed to load quote, Reason For Failure:{}".format(e))
            print(item)
        return item


class ScraperJobPipeline:

    def process_item(self, item, spider):
        try:
            Jobs.objects.create(

                title=item['title'],
                text=item['text'],
                image=item['image'],
                applylink=item['applylink'])
            print("\n")
            logger.warn("Loaded quote {}".format(item['text']))
            print(item)
        except Exception as e:
            print("\n")
            logger.error(
                "\nFailed to load quote, Reason For Failure:{}".format(e))
            print(item)
        return item

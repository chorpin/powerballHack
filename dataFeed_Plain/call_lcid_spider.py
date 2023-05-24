from scrapy.crawler import CrawlerProcess
from dataFeed_Plain.lcid_spider import LCIDSpider

process = CrawlerProcess()
process.crawl(LCIDSpider)
process.start()

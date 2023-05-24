import scrapy
from pymongo import MongoClient


class LCIDSpider(scrapy.Spider):
    name = "lcid"
    start_urls = ["https://www.bbc.com/", "https://www.nytimes.com/", "https://www.theguardian.com/", "https://www.reuters.com/", "https://www.cnn.com/",
                  "https://www.aljazeera.com/", "https://www.npr.org/", "https://www.economist.com/", "https://www.washingtonpost.com/", "https://www.factcheck.org/"]

    def __init__(self):
        self.client = MongoClient()
        self.db = self.client.lcid_db

    def parse(self, response):
        for link in response.css('a::attr(href)').getall():
            yield response.follow(link, self.parse)

        matches = response.css('*::text').getall()
        matches = [match for match in matches if 'LCID' in match]
        if matches:
            self.db.matches.insert_one({
                'url': response.url,
                'matches': matches
            })

    def closed(self, reason):
        self.client.close()


'''
This script imports the MongoClient class from the pymongo library and creates an instance of the MongoClient class in the spider's __init__ method. This connects to a MongoDB server running on the default host and port. We are also creating a database named 'lcid_db' and collection named 'matches'

In the parse() method, instead of yielding the results, this script uses the insert_one() method to insert a new document into the 'matches' collection. The document contains the URL and matches found on that page.

In the closed() method, the script closes the MongoClient connection when the spider is closed.

'''

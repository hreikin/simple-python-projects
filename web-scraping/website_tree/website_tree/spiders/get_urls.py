import scrapy
from scrapy.spiders import SitemapSpider


class GetUrlsSpider(SitemapSpider):
    name = 'get_urls'
    allowed_domains = ['princetonscientific.com']
    sitemap_urls = ['https://princetonscientific.com/sitemap_index.xml']

    def parse(self, response):
        page_title = response.css('title::text').get()
        page_url = response.url
        urls = {
            page_title: page_url
        }

        file = "new-urls.txt"
        with open(file, "a") as stream:
            for v in urls.values():
                stream.write(v + " ")

        yield urls

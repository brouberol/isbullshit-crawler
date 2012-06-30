import urlparse

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector
from isbullshit.items import IsBullshitItem


class IsBullshitSpider(CrawlSpider):
    """ General configuration of the Crawl Spider """
    name = 'isbullshit'
    start_urls = ['http://isbullsh.it'] # urls from which the spider will start crawling
    rules = [Rule(SgmlLinkExtractor(allow=[r'page/\d+']), follow=True), 
        # r'page/\d+' : regular expression for http://isbullsh.it/page/X URLs
        Rule(SgmlLinkExtractor(allow=[r'\d{4}/\d{2}/\w+']), callback='parse_blogpost')]
        # r'\d{4}/\d{2}/\w+' : regular expression for http://isbullsh.it/YYYY/MM/title URLs

    def parse_blogpost(self, response):
        """ Extract title, author, tag(s), date, location, url and the html text of a blogpost,
        using XPath selectors
        """
        hxs = HtmlXPathSelector(response)
        item = IsBullshitItem()
        # Extract title
        item['title'] = hxs.select('//header/h1/text()').extract()[0]
        # Extract author
        item['author'] = hxs.select('//header/p/a/text()').extract()[0]
        # Extract tag(s)
        item['tag'] = hxs.select("//header/div[@class='post-data']/p/a/text()").extract() 
        # Extract date
        item['date'] = hxs.select("//header/div[@class='post-data']/p[contains(text(), '20')]/text()").extract()[0]
        # Extract location
        item['location'] = hxs.select("//header/div[@class='post-data']/p[contains(text(), 'From')]/text()").extract()[0].replace('From', '') 
        # Extract article url
        urls = hxs.select("//div[@class='breadcrumb-container']/ul[@class='breadcrumb']/li/a/@href").extract()
        item['url'] = urlparse.urljoin(urls[1], urls[2])
        # Extract article text, with html tags
        item['article_html'] = hxs.select("//div[@role='main']/article").extract()[0]
        
        return item


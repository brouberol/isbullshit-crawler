from scrapy.item import Item, Field

class IsBullshitItem(Item):
    """ Definition of all the fields we want to extract from a scraped webpage. """
    title = Field()
    author = Field()
    tag = Field()
    date = Field()
    url = Field()
    location = Field()
    article_html = Field()
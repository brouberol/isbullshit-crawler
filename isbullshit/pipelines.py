import pymongo

from scrapy.exceptions import DropItem
from scrapy.conf import settings
from scrapy import log

class MongoDBStorage(object):
    def __init__(self):
        """ Initiate a MongoDB connection, a create the settings['MONGODB_COLLECTION'] collection. """
        connection = pymongo.Connection(settings['MONGODB_SERVER'], settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]
        
    def process_item(self, item, spider):
        """ This method is called each time an item is scraped from a webpage.
        If the item validates, we store it in the MongoDB collection. If not,
        we drop it.
        """
        # Validate article
        if not item['article_html']:
            raise DropItem("Missing article text of article from %" %item['url'])
        elif not item['title']:
            raise DropItem("Missing title of object from %" %item['url'])
        else:

            # If valid article, insert it in MongoDB collection
            # Log this insertion
            self.collection.insert(dict(item))
            log.msg("Item wrote to MongoDB database %s/%s" %
                    (settings['MONGODB_DB'], settings['MONGODB_COLLECTION']),
                    level=log.DEBUG, spider=spider) 
        return item
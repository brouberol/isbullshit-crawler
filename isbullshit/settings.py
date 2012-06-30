# Scrapy settings for isbullshit project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'isbullshit'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['isbullshit.spiders']
NEWSPIDER_MODULE = 'isbullshit.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = [
    'isbullshit.pipelines.MongoDBStorage',
]

MONGODB_SERVER = "localhost"
MONGODB_PORT = 27017
MONGODB_DB = "isbullshit"
MONGODB_COLLECTION = "articles"

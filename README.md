This project contains the code of the spider described in my blogpost [Crawl a website with Scrapy](http://isbullsh.it/2012/04/Web-crawling-with-scrapy/).

This spider crawls the website [http://isbullsh.it](http://isbullsh.it), and extract information about each blogpost:

* title
* author
* tag(s)
* release date
* url
* HTML formatted text
* location 

We implement the spider using [Scrapy](http://scrapy.org).

# Requirements

* Scrapy: `pip install Scrapy`
* pymongo: `pip install pymongo`
* An installed MongoDB server

# How do I test it?
Release the spider by entering

    scrapy crawl isbullshit


# -*- coding:utf-8 -*-

from crawler.crawler import crawler
from callback.scraping_callback import scraping_callback

if __name__ == '__main__':
    crawler(callback=scraping_callback)

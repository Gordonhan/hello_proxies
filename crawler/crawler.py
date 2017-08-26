# -*- coding:utf-8 -*-
from time import sleep

from config import SEED_URLS
from downloader import download


def crawler(seed_url=SEED_URLS, callback=None):
    crawl_queue = list(seed_url)

    while True:
        for url in crawl_queue:
            html = download(url)
            if callback:
                callback(url, html)

        sleep(60 * 10)

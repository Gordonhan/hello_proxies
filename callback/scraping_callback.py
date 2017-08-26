# -*- coding:utf-8 -*-
import lxml.html


def scraping_callback(url, html):
    tree = lxml.html.fromstring(html)
    if url == 'http://www.ip181.com/':
        elem = tree.cssselect('table.table-hover > tbody > tr')[1:]
        for e in elem:
            for td in e.getchildren():
                # print td.text_content()
                pass

    elif url == 'http://www.xicidaili.com/':
        pass
    elif url == 'http://www.kxdaili.com/':
        pass
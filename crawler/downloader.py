# -*- coding:utf-8 -*-
import requests

import utils.header


def download(url):
    print 'Downloading', url
    header = utils.header.get_header()
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        # 当requests使用ISO-8859-1
        if r.encoding == 'ISO-8859-1':
            encodings = requests.utils.get_encodings_from_content(r.text)
            if encodings:
                encoding = encodings[0]
            else:
                encoding = r.apparent_encoding
        else:
            encoding = r.encoding
        return r.content.decode(encoding, 'replace').encode('utf-8', 'replace')
    else:
        r.raise_for_status()

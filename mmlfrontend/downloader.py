#!/usr/bin/env python
# encoding: utf-8
__author__ = 'nakasho'

import urllib.request
from urllib.request import FileHandler
from html.parser import HTMLParser


class Downloader(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.files = []
        self._path = ""

    def handle_starttag(self, tag, attrs):
        if tag == 'a' and attrs[0][0] == 'href' and attrs[0][1].endswith('.html'):
            self.files.append(attrs[0][1])

    def read_index(self, path):
        self._path = path
        response = urllib.request.urlopen(path)
        try:
            data = response.read()
            data = data.decode(encoding='UTF-8')
            self.feed(data)
        finally:
            response.close()

    def download(self, to_dir):
        for filename in self.files:
            urllib.request.urlretrieve(self._path + '/' + filename, to_dir + '/' + filename)

if __name__ == "__main__":
    downloader = Downloader()
    downloader.read_index('http://mizar.org/version/current/html/mml-articles')
    downloader.download()
    downloader.close()

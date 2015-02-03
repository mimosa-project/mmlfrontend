#!/usr/bin/env python
# encoding: utf-8
__author__ = 'nakasho'

import glob
import os
import os.path
import time
from mmlfrontend.reader import *
from mmlfrontend.composer import *
from mmlfrontend.writer import *
import locale
from natsort import humansorted
locale.setlocale(locale.LC_ALL, '')


class Processor:
    def __init__(self):
        self.elements = []
        self.contents = []

    def execute(self, path):
        self.read(path)
        self.compose()
        self.write(path)

    def read(self, path):
        htmls = glob.glob(path + "/mml-articles/*.html")
        htmls = humansorted(htmls)

        total_count = len(htmls)
        for i, html in enumerate(htmls):
            print("reading {}/{}".format(i, total_count))
            reader = Reader()
            reader.read(html)
            self.elements += reader.elements

    def compose(self):
        print("composing...")
        composer = Composer()
        composer.elements = self.elements
        composer.build()
        self.contents = composer.contents

    def write(self, path):
        index_writer = IndexWriter()
        index_writer.contents = self.contents
        index_writer.write(path + '/js/mml-index.js')

        contents_dir = path + '/mml-contents'
        if not os.path.exists(contents_dir):
            time.sleep(0.01)
            os.mkdir(contents_dir)

        total_count = len(self.contents)
        for i, content in enumerate(self.contents):
            if i % 10 == 0:
                print("writing {}/{}".format(i, total_count))
            content_writer = ContentWriter()
            content_writer.content = content
            content_writer.write(contents_dir + '/' + content.filename())

if __name__ == '__main__':
    path = os.path.dirname(__file__) + '/../html'
    processor = Processor()
    processor.execute(path)

#!/usr/bin/env python
# encoding: utf-8
__author__ = 'nakasho'

from unittest import TestCase
from mmlfrontend.processor import Processor
import os
import os.path
import shutil


class TestProcessor(TestCase):
    @classmethod
    def setUpClass(cls):
        cls._local_dir = os.path.dirname(__file__)
        cls._local_dir = cls._local_dir.replace('\\', '/')

    @classmethod
    def tearDownClass(cls):
        pass

    @staticmethod
    def filter_by_type(elements, typename):
        return [e for e in elements if e.type() == typename]

    def test_read(self):
        dir_path = self._local_dir + '/data/processor'
        processor = Processor()
        processor.read(dir_path)

        self.assertEqual(36, len(self.filter_by_type(processor.elements, 'pred')))
        self.assertEqual(10, len(self.filter_by_type(processor.elements, 'struct')))
        self.assertEqual(40, len(self.filter_by_type(processor.elements, 'mode')))
        self.assertEqual(185, len(self.filter_by_type(processor.elements, 'func')))
        self.assertEqual(96, len(self.filter_by_type(processor.elements, 'attr')))
        self.assertEqual(279, len(self.filter_by_type(processor.elements, 'cluster')))

    def copy_resources(self):
        files = ["index.html", "start.html", "js/mml-reference.js", "css/mml-reference.css"]
        for file in files:
            src = self._local_dir + "/../html/" + file
            dst = self._local_dir + "/data/processor/" + file
            shutil.copyfile(src, dst)

    def test_execute(self):
        self.copy_resources()
        contents_dir = self._local_dir + '/data/processor/mml-contents'
        if os.path.exists(contents_dir):
            shutil.rmtree(contents_dir)

        path = self._local_dir + '/data/processor'
        processor = Processor()
        processor.execute(path)

    def test_copy_only(self):
        self.copy_resources()

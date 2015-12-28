import unittest
import os

import ioworks as io
import testfile as tf
from cmakefile import CmakeFile as cf
from configurator import Params
from utils import this_script_dir

cmp_dir = "/".join([this_script_dir(),"tests"]).replace('//', '/')

class TestCmakeFile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srcCMakePath       = Params.get_cmake_template()
        cls.expectCmakePath    = os.path.join(cmp_dir, "compare.txt")
        cls.expectContent      = io.get_lines(cls.expectCmakePath)
        cls.msg ='\n\n===== Compared {0} and {1}'

    def test_prepare(self):
        actual = cf.prepare(self.srcCMakePath, "kncore", ["kncore", "kngeo"])
        self.assertListEqual(actual, self.expectContent,
                             msg=self.msg.format(self.srcCMakePath,
                                                 self.expectCmakePath))


class Testfile(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.srcTestPath        = Params.get_test_template()
        cls.expectedTestPath   = os.path.join(cmp_dir, "testcompare.cpp")
        cls.expectedContent    = io.get_lines(cls.expectedTestPath)
        cls.testCaseName = "NewTestCase"
        cls.msg ='\n\n===== Use name "{2}", Compared {0} and {1}'

    def test_prepare(self):
        actual = tf.TestFile.prepare(self.srcTestPath, self.testCaseName)
        self.assertListEqual(actual, self.expectedContent,
                             msg=self.msg.format(self.srcTestPath,
                                                 self.expectedTestPath,
                                                 self.testCaseName))


class TestAddSubdirectory(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # self.srcCMakePath       = os.path.join(cmp_dir, Params.filenameCmake)
        cls.expectCmakePath    = os.path.join(cmp_dir, "addsubcompare.txt")
        cls.expectContent      = io.get_lines(cls.expectCmakePath)
        cls.testDirName        = "test"
        cls.msg ='\n\n===== Compared {0} and {1}'

    def test_prepare(self):
        actual = cf.prepareParent(cmp_dir, self.testDirName)
        self.assertListEqual(actual, self.expectContent,
                             msg=self.msg.format("{generated}",
                                                 self.expectCmakePath))


class TestIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass")

    def setUp(self):
        print("setUp")

    def test_one(self):
        print("test one")

    def test_two(self):
        print("test two")

    def test_three(self):
        print("test three")

    def tearDown(self):
        print("tearDown")


if __name__ == '__main__':
    unittest.main()

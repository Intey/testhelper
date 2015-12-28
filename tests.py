import unittest
import os

import ioworks as io
import testfile as tf
from cmakefile import CmakeFile as cf
from configurator import Params
from utils import this_script_dir

cmp_dir = "/".join([this_script_dir(),"tests"]).replace('//', '/')

class TestCmakeFile(unittest.TestCase):
    def setUp(self):
        self.srcCMakePath       = Params.get_cmake_template()
        self.expectCmakePath    = os.path.join(cmp_dir, "compare.txt")
        self.expectContent      = io.get_lines(self.expectCmakePath)
        self.msg ='\n\n===== Compared {0} and {1}'

    def test_prepare(self):
        actual = cf.prepare(self.srcCMakePath, "kncore", ["kncore", "kngeo"])
        self.assertListEqual(actual, self.expectContent,
                             msg=self.msg.format(self.srcCMakePath,
                                                 self.expectCmakePath))


class Testfile(unittest.TestCase):
    def setUp(self):
        self.srcTestPath        = Params.get_test_template()
        self.expectedTestPath   = os.path.join(cmp_dir, "testcompare.cpp")
        self.expectedContent    = io.get_lines(self.expectedTestPath)
        self.testCaseName = "NewTestCase"
        self.msg ='\n\n===== Use name "{2}", Compared {0} and {1}'

    def test_prepare(self):
        actual = tf.TestFile.prepare(self.srcTestPath, self.testCaseName)
        self.assertListEqual(actual, self.expectedContent,
                             msg=self.msg.format(self.srcTestPath,
                                                 self.expectedTestPath,
                                                 self.testCaseName))


class TestAddSubdirectory(unittest.TestCase):
    def setUp(self):
        # self.srcCMakePath       = os.path.join(cmp_dir, Params.filenameCmake)
        self.expectCmakePath    = os.path.join(cmp_dir, "addsubcompare.txt")
        self.expectContent      = io.get_lines(self.expectCmakePath)
        self.testDirName        = "test"
        self.msg ='\n\n===== Compared {0} and {1}'

    def test_prepare(self):
        actual = cf.prepareParent(cmp_dir, self.testDirName)
        self.assertListEqual(actual, self.expectContent,
                             msg=self.msg.format("{generated}",
                                                 self.expectCmakePath))


if __name__ == '__main__':
    unittest.main()

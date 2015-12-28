import unittest
import ioworks as io
from cmakefile import CmakeFile as cf
import testfile as tf
from configurator import Params

cmp_dir = "tests/"

class TestCmakeFile(unittest.TestCase):
    def setUp(self):
        self.srcCMakePath       = Params.get_cmake_template()
        self.expectCmakePath    = cmp_dir + "compare.txt"
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
        self.expectedTestPath   = cmp_dir + "testcompare.cpp"
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
        self.srcCmakePath       = Params.get_parent_cmake_template()
        self.expectedCmakePath  = cmp_dir + "addsubcompare.txt"
        self.expectContent      = io.get_lines(self.expectedCmakePath)
        self.testDirname        = ""
        self.msg ='\n\n===== Compared {0} and {1}'
    def test_prepare(self):
        actual = cf.prepareParent(self.srcCMakePath, self.testDirname)
        self.assertListEqual(actual, self.expectContent,
                             msg=self.msg.format(self.srcCMakePath,
                                            self.expectCmakePath))


if __name__ == '__main__':
    unittest.main()

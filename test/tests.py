import unittest
import ioworks as io
import cmakefile as cf
from testfile import TestFile as tf

import pprint


class TestCmakeFile(unittest.TestCase):

    def setUp(self):
        self.srcCMakePath = "CMakeLists.txt"
        self.expectCmakePath = "compare.txt"
        self.expectContent = io.get_lines(self.expectCmakePath)

    def test_prepare(self):
        actual = cf.prepare(self.srcCMakePath, "kncore", ["kncore", "kngeo"])
        # pprint.pprint(actual)
        # pprint.pprint(self.expectContent)
        self.assertListEqual(actual, self.expectContent)


class Testfile(unittest.TestCase):

    def setUp(self):
        self.srcTestPath = "test.cpp"
        self.expectedTestPath = "testcompare.cpp"
        self.expectedContent = io.get_lines(self.expectedTestPath)
        self.testCaseName = "NewTestCase"

    def test_prepare(self):
        self.assertListEqual(tf.prepare(self.srcTestPath, self.testCaseName), self.expectedContent)


if __name__ == '__main__':
    unittest.main() 

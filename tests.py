import unittest
import ioworks as io
import cmakefile as cf
import testfile as tf
import configuragor as conf

cmp_dir = "tests/"

class TestCmakeFile(unittest.TestCase):
    def setUp(self):
        self.srcCMakePath = conf.get_cmake_template()
        self.expectCmakePath = cmp_dir + "compare.txt"
        self.expectContent = io.get_lines(self.expectCmakePath)

    def test_prepare(self):
        actual = cf.prepare(self.srcCMakePath, "kncore", ["kncore", "kngeo"])
        self.assertListEqual(actual, self.expectContent)


class Testfile(unittest.TestCase):
    def setUp(self):
        self.srcTestPath = conf.get_test_template()
        self.expectedTestPath = cmp_dir + "testcompare.cpp"
        self.expectedContent = io.get_lines(self.expectedTestPath)
        self.testCaseName = "NewTestCase"

    def test_prepare(self):
        self.assertListEqual(tf.TestFile.prepare(self.srcTestPath,
                                                 self.testCaseName),
                             self.expectedContent)


if __name__ == '__main__':
    unittest.main()

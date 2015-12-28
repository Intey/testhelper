import unittest
import ioworks as io
from cmakefile import CmakeFile as cf
import testfile as tf
from configurator import Params

cmp_dir = "tests/"

class TestCmakeFile(unittest.TestCase):
    def setUp(self):
        self.srcCMakePath = Params.get_cmake_template()
        self.expectCmakePath = cmp_dir + "compare.txt"
        self.expectContent = io.get_lines(self.expectCmakePath)

    def test_prepare(self):
        actual = cf.prepare(self.srcCMakePath, "kncore", ["kncore", "kngeo"])
        self.assertListEqual(actual, self.expectContent,
                             msg='{0}, {1}'.format(self.srcCMakePath,
                                                   self.expectCmakePath))


class Testfile(unittest.TestCase):
    def setUp(self):
        self.srcTestPath = Params.get_test_template()
        self.expectedTestPath = cmp_dir + "testcompare.cpp"
        self.expectedContent = io.get_lines(self.expectedTestPath)
        self.testCaseName = "NewTestCase"

    def test_prepare(self):
        actual = tf.TestFile.prepare(self.srcTestPath, self.testCaseName)
        self.assertListEqual(actual, self.expectedContent,
                             msg='\n Compared {0} and {1}'
                                 .format(self.srcTestPath,
                                         self.expectedTestPath))


if __name__ == '__main__':
    unittest.main()

import unittest
import ioworks as io
import cmakefile as cf
import testfile as tf


class TestCmakeFile(unittest.TestCase):
    def setUp(self):
        self.srcCMakePath = "CMakeLists.txt"
        self.expectCmakePath = "compare.txt"
        self.expectContent = io.get_lines(self.expectCmakePath)

    def test_prepare(self):
        actual = cf.prepare(self.srcCMakePath, "kncore", ["kncore", "kngeo"])
        self.assertListEqual(actual, self.expectContent)


class Testfile(unittest.TestCase):
    def setUp(self):
        self.srcTestPath = "test.cpp"
        self.expectedTestPath = "testcompare.cpp"
        self.expectedContent = io.get_lines(self.expectedTestPath)
        self.testCaseName = "NewTestCase"

    def test_prepare(self):
        self.assertListEqual(tf.TestFile.prepare(self.srcTestPath,
                                                 self.testCaseName),
                             self.expectedContent)


if __name__ == '__main__':
    unittest.main()

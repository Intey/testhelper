import unittest
import cmakefile as cf
import testfile as tf
import pprint


def readfile(path):
        f = open(path, 'r')
        result = f.readlines()
        f.close()
        return result


class TestCmakeFile(unittest.TestCase):

    def setUp(self):
        self.srcCMakePath = "CMakeLists.txt"
        self.expectCmakePath = "compare.txt"
        self.expectContent = readfile(self.srcCMakePath)

    def test_prepare(self):
        actual = cf.prepare(self.srcCMakePath, "kncore", ["kncore", "kngeo"])
        pprint.pprint(actual)
        pprint.pprint(self.expectContent)

        self.assertListEqual(actual, self.expectContent)


class Testfile(unittest.TestCase):

    def setUp(self):
        self.srcTestPath = "test.cpp"
        self.expectedTestPath = "testcompare.cpp"
        self.expectedContent = readfile(self.expectedTestPath)

    def test_prepare(self):
        self.assertListEqual(tf.prepare(self.srcTestPath), self.expectedContent)


if __name__ == '__main__':
    unittest.main() 

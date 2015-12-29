import unittest
import os
import shutil

import ioworks as io
import testfile as tf
from cmakefile import CmakeFile as cf
from configurator import Params
from utils import this_script_dir
import createTest as ct

_test_path = "/".join([this_script_dir(),"tests"]).replace('//', '/')


def assetsUp(fn):
    """Add 'assets' field to class, and create directory with cls.__name__.
    Skip, if directory exists."""
    def wrap(cls):
        cls.assets = os.path.join(_test_path, cls.__name__)
        try: os.mkdir(cls.assets)
        except OSError as e: pass
        fn(cls)

    return wrap


def assetsDown(fn):
    """Remove directory, that represented in 'assets' field of class."""
    def wrap(cls):
        try: shutil.rmtree(cls.assets)
        except OSError as e:
            print("can't remove 'cls.assets'. You should use assetsUp decorator,"
                  + " on setUpClass.", e)
        fn(cls)

    return wrap


class TestCmakeFile(unittest.TestCase):
    @classmethod
    @assetsUp
    def setUpClass(cls):
        cls.srcCMakePath       = Params.get_cmake_template()
        cls.expectCmakePath    = os.path.join(cls.assets, Params.filenameCmake)
        cls.expectContent      = io.get_lines(cls.expectCmakePath)
        cls.msg ='\n\n===== Compared {0} and {1}'

    def test_prepare(self):
        actual = cf.prepare(self.srcCMakePath, "kncore", ["kncore", "kngeo"])

        self.assertListEqual(actual, self.expectContent,
                             msg=self.msg.format(self.srcCMakePath,
                                                 self.expectCmakePath))


class Testfile(unittest.TestCase):
    """ Not use tearDown assets decorator, 'couze we doesn't need to delete them"""
    @classmethod
    @assetsUp
    def setUpClass(cls):
        cls.srcTestPath        = Params.get_test_template()
        cls.expectedTestPath   = os.path.join(cls.assets, "testfile.cpp")
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
    @assetsUp
    def setUpClass(cls):
        # self.srcCMakePath    = os.path.join(cls.assets, Params.filenameCmake)
        cls.expectCmakePath    = os.path.join(cls.assets, "addsubcompare.txt")
        cls.expectContent      = io.get_lines(cls.expectCmakePath)
        cls.testDirName        = "test"
        cls.msg ='\n\n===== Compared {0} and {1}'

    def test_prepare(self):
        actual = cf.prepareParent(self.testDirName)

        self.assertListEqual(actual, self.expectContent,
                             msg=self.msg.format("{generated}",
                                                 self.expectCmakePath))


@unittest.skip("")
class TestIntegration(unittest.TestCase):
    """ Check test creation.
    Need folders <this_script_dir>/tests/ingry/{testing,compare/testing}.
    compare - contains expected files.
    testing - folder, where test will be created"""

    @classmethod
    @assetsUp
    def setUpClass(cls):
        cls.tcn_testing           = "testing"
        # +=======================================+
        # | path, where actuall test expect to be |
        # +=======================================+
        # parent cmake can be found *near* test folder(cls.assets)
        cls.parent_cmake_filepath = os.path.join(_test_path,
                                                 Params.filenameCmake)
        cls.cmake_filepath        = os.path.join(cls.assets, Params.filenameCmake)
        cls.test_filepath         = os.path.join(cls.assets, cls.tcn_testing)

        # +=======================================+
        # | paths, where compare assets should be |
        # +=======================================+
        cmpdir                    = os.path.join(_test_path, "compare")
        cmptestdir                = os.path.join(cmpdir, cls.tcn_testing)
        # parent cmake filepath
        cls.cmp_pcfp              = os.path.join(cmpdir, Params.filenameCmake)
        # cmake filepath
        cls.cmp_cfp               = os.path.join(cmptestdir,
                                                 Params.filenameCmake)
        # test filepath
        cls.cmp_tfp               = os.path.join(cmptestdir, cls.tcn_testing)

    def setUp(self):
        pass

    def tearDown(self):
        shutil.rmtree(self.assets)

    def cmp_files(self, fisrt, second):
        self.assertListEqual(io.get_lines(first), io.get_lines(second))

    def tester(self, tcn, mods, grp):
        ct.create_test(self.assets, tcn, mods, grp)
        cmp_files(self.parent_cmake_filepath, self.cmp_pcfp)
        cmp_files(self.cmake_filepath,        self.cmp_cfp)
        cmp_files(self.test_filepath,         self.cmp_tfp)

    def test_poorInput(self):
        self.tester("testing", [], "")

    def test_mods(self):
        self.tester("testing", ["one", "second", "third"], "")

    def test_group(self):
        groupname = "grouped"

        ct.create_test(self.assets, "testing", [], groupname)

        cmake_fp = os.path.join(self.assets, groupname, Params.filenameCmake)
        test_fp  = os.path.join(self.assets, groupname, "testing.cpp")

        cmp_files(self.parent_cmake_filepath, self.cmp_pcfp)
        cmp_files(cmake_fp,                   self.cmp_cfp)
        cmp_files(self.test_filepath,         self.cmp_tfp)


if __name__ == '__main__':
    unittest.main()

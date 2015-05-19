#!/usr/bin/python3
"""
Usage:
    createTest.py TESTCASENAME [(-g GROUP)] [(--config FILE)] [(--use MODULE...)]
    createTest.py (-h | --help)
Options:
    TESTCASENAME            Name of creating test case
    [(-g GROUP)]            Name of module or group, that for test is created. This used for group sources in VS.
    [(--config FILE)]       Use Config file FILE
    [(--use MODULE...)]     Include modules to test
    -h, --help              Show this help text
    -v, --version           Stow version
"""
# File work
from os import getcwd, makedirs

# from string import Template  # string interpolation
import ioworks as io
from docopt import docopt

from cmakefile import CmakeFile
from testfile import TestFile
from configurator import Params


def mk_test_folder(group, test_case_name):
    """ Creates path for new test
    :param: group - directory in tests dir where be placed dir with testcasename.
            testcasename - directory in group dir.
    :return: Path to new folder, where should be placed new test.
    """
    path = "/".join([Params.testDir, group, test_case_name + Params.testDirPostfix]).strip('/').replace('//', '/')
    makedirs(path, exist_ok=True)
    return path


def copy_files(dst):
    """
    Move all template files to destination folder
    :return: dst path
    """
    dst = "/".join([getcwd(), dst]).strip('\\').replace('\\', '/')

    from distutils.dir_util import copy_tree

    copy_tree(Params.templatesDir, dst)
    return dst


if __name__ == '__main__':
    # test string
    arguments = docopt(__doc__, argv="knCoreTest -g kncore --config conf --use kncore kngeo kngui ", version='0.1')
    # arguments = docopt(__doc__, version='0.1')
    # read_config()

    testCaseName = arguments["TESTCASENAME"]
    modules = arguments["MODULE"]
    group = arguments["GROUP"]
    conf_file = arguments["FILE"]
    pwd = getcwd()

    dst = copy_files(mk_test_folder(group, testCaseName))

    cmakeout = CmakeFile.prepare(Params.get_cmake_template(), group, modules)
    io.write_to_file("/".join([dst, Params.filenameCmake]), cmakeout)
    testout = TestFile.prepare(Params.get_test_template(), testCaseName)
    io.write_to_file("/".join([dst, testCaseName + Params.testDirPostfix + ".cpp"]), testout)
    print("Ok, ready for change files")

    # mainfile.prepare()

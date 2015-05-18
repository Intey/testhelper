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
from shutil import copytree
from string import Template  # string interpolation

from docopt import docopt

import cmakefile as CmakeFile
from testfile import TestFile


class Params:
    confFile = "config.conf"
    templatesDir = "_testTemplate"
    confSections = ["files"]
    filenameCmake = "CMakeLists.txt"
    filenameMain = "main.cpp"
    filenameTest = "test.cpp"
    testDir = "tests"

    @staticmethod
    def get_cmake_template():
        return "/".join([Params.templatesDir, Params.filenameCmake])

    @staticmethod
    def get_test_template():
        return "/".join([Params.templatesDir, Params.filenameTest])


def mk_test_folder(group, test_case_name):
    """ Creates path for new test
    :param: group - directory in tests dir where be placed dir with testcasename.
            testcasename - directory in group dir.
    :return: Path to new folder, where should be placed new test.
    """
    path = "/".join([Params.testDir, group, test_case_name]).strip('/').replace('//', '/')
    makedirs(path, exist_ok=True)
    return path


def copy_files(dst):
    """
    Move all template files to destination folder
    :return: dst path
    """
    dst = "/".join([getcwd(),dst]).strip('\\').replace('\\', '/')
    from distutils.dir_util import copy_tree
    copy_tree(Params.templatesDir, dst)
    return dst

# main actions



def writeToFile(path, lines):
    fileCmake = open(path, 'w', encoding="UTF8")
    fileCmake.writelines(lines)
    fileCmake.close()


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
    writeToFile("/".join([dst, Params.filenameCmake]), cmakeout)
    testout = TestFile.prepare(Params.get_test_template(), testCaseName)
    writeToFile("/".join([dst, Params.filenameTest]), testout)
    print("Ok, ready for change files")


    # mainfile.prepare()

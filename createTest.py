#!/usr/bin/python3

# createTest.py TESTCASENAME [(-g GROUP)] [(--config FILE)] [(--use MODULE...)]

"""
createTest.py:
	Create test in ./tests

Usage:
    createTest.py TESTCASENAME [(-g GROUP)] [(--use MODULE...)]
    createTest.py (-h | --help)


Options:
    TESTCASENAME            Name of creating test case
    [(-g GROUP)]            Name of module or group, that for test is created.
                            This used for group sources in VS.
    [(--config FILE)]       Use Config file FILE
    [(--use MODULE...)]     Include modules to test
    -h, --help              Show this help text
    -v, --version           Stow version
"""

# File work
import os
from string import Template  # string interpolation

from docopt import docopt

import ioworks as io
from cmakefile import CmakeFile
from testfile import TestFile
from configurator import Params

def mkTestFolder(dst, group, test_case_name):
    path = os.path.join(dst, group, test_case_name)
    os.makedirs(path, exist_ok=True)
    return path


def copy_files(dst):
    """ Move all template files to destination folder """
    from distutils.dir_util import copy_tree

    copy_tree(Params.templatesDir, dst)


def attach_to_cmake(dst, testCaseFolder):
    """Add line with 'add_subdirectory(%testcasename%_test)' to CmakeLists.txt in
    directory where this test folder was created.
    :param: dst - path to dir, where will be created test folder."""
    parent_cmake = os.path.join(dst, "CMakeLists.txt")
    io.append_to_file(parent_cmake, CmakeFile.prepareParent(testCaseFolder))


def create_test(dst, tcn, mods, grp):
    """ Main create function. Prepare all files and put them in dst.
    :param: dst - destination folder. Should be abspath directory
    :param: tcn - testcase name.
    :param: mods - dependencies that whas added in cmake target_link_library
    :param: grp - group of tests, just name of subfolder in dst
    """

    tcn = tcn.lower()
    testFolderName = tcn + Params.testDirPostfix
    testFilename = testFolderName + ".cpp"
    testFolder =  mkTestFolder(dst, grp, testFolderName)

    copy_files(testFolder)

    # TODO: to one func: CmakeFile.create
    cmake_content = CmakeFile.prepare(Params.get_cmake_template(), grp, mods)
    io.write_to_file(os.path.join(testFolder, Params.filenameCmake), cmake_content)

    # TODO: to one func: TestFile.create
    test_content = TestFile.prepare(Params.get_test_template(), tcn)
    io.write_to_file(os.path.join(testFolder, testFilename), test_content)

    attach_to_cmake(os.path.join(dst,grp), testFolderName)


if __name__ == '__main__':
    # arguments = docopt(__doc__, argv="knCoreTest -g kncore --config conf --use kncore kngeo kngui ", version='0.1')

    arguments = docopt(__doc__, version='0.1')
    test_case_name = arguments["TESTCASENAME"]
    modules = arguments["MODULE"]
    group = arguments["GROUP"] or ""

    dst = os.path.join(os.getcwd(), Params.testDir)

    create_test(dst, test_case_name, modules, group)

    message = Template("Test case $tcn created in $path")\
                .substitute(tcn=test_case_name, path=dst)

    print(message)

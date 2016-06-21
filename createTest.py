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


def mk_test_folder(group, test_case_name):
    """ Creates path for new test
    :param: group - directory in tests dir where be placed dir with testcasename.
            testcasename - directory in group dir.
    :return: Path to new folder, where should be placed new test.
    """
    # generate test in current dir + tests (./tests/<testcasename_test>)
    dirname = test_case_name + Params.testDirPostfix
    path = os.path.join(Params.testDir, group, dirname)
    os.makedirs(path, exist_ok=True)
    return path


def copy_files(dst):
    """ Move all template files to destination folder """
    from distutils.dir_util import copy_tree

    copy_tree(Params.templatesDir, dst)


def attach_to_cmake(dst, tcn):
    """Add line with 'add_subdirectory(testcasename)' to CmakeLists.txt in
    directory where this test folder was created.
    :param: dst - path to dir, where will be created test folder."""
    io.write_to_file(dst+"CMakeLists.txt", "add_subdirectory("+tcn+")")


def create_test(dst, tcn, mods, grp):
    dst           = os.path.join(os.getcwd(), dst).strip('\\').replace('\\', '/')
    test_filename = tcn.lower() + Params.testDirPostfix + ".cpp"
    copy_files(mk_test_folder(grp, tcn))

    # TODO: to one func: CmakeFile.create
    cmakeout = CmakeFile.prepare(Params.get_cmake_template(), grp, mods)
    io.write_to_file(os.path.join(dst, Params.filenameCmake), cmakeout)

    # TODO: to one func: TestFile.create
    testout = TestFile.prepare(Params.get_test_template(), tcn)
    io.write_to_file(os.path.join(dst, test_filename), testout)


if __name__ == '__main__':
    # arguments = docopt(__doc__, argv="knCoreTest -g kncore --config conf --use kncore kngeo kngui ", version='0.1')

    arguments = docopt(__doc__, version='0.1')
    test_case_name = arguments["TESTCASENAME"]
    modules = arguments["MODULE"]
    group = arguments["GROUP"]

    create_test(dst, test_case_name, modules, group)

    message = Template("Test case $tcn created in $path")\
                .substitute(tcn=test_case_name, path=dst)

    print(message)

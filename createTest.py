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
    [(-g GROUP)]            Name of module or group, that for test is created. This used for group sources in VS.
    [(--config FILE)]       Use Config file FILE
    [(--use MODULE...)]     Include modules to test
    -h, --help              Show this help text
    -v, --version           Stow version
"""

# File work
from os import getcwd, makedirs
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
    # generate test in current dir + tests (./tests/<testcasename>)
    path = "/".join([Params.testDir,
                    group,
                    test_case_name + Params.testDirPostfix]
                    ).strip('/').replace('//', '/')
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


def attach_to_cmake(dst, tcn):
    """Add line with 'add_subdirectory(TESTCASENAME)' to CmakeLists.txt in
    directory where this test folder was created."""
    io.write_to_file(dst+"CMakeLists.txt", "add_subdirectory("+tcn+")")


if __name__ == '__main__':
    # arguments = docopt(__doc__, argv="knCoreTest -g kncore --config conf --use kncore kngeo kngui ", version='0.1')

    arguments = docopt(__doc__, version='0.1')
    testCaseName = arguments["TESTCASENAME"]
    modules = arguments["MODULE"]
    group = arguments["GROUP"]
    pwd = getcwd()

    dst = copy_files(mk_test_folder(group, testCaseName))

    cmakeout = CmakeFile.prepare(Params.get_cmake_template(), group, modules)
    io.write_to_file("/".join([dst, Params.filenameCmake]), cmakeout)
    testout = TestFile.prepare(Params.get_test_template(), testCaseName)
    io.write_to_file("/".join([dst, testCaseName.lower() + Params.testDirPostfix + ".cpp"]), testout)

    message = Template("Test case $tcn created in $path ").substitute(tcn=testCaseName, path=dst)

    print(message)

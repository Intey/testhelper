#!/usr/bin/env python
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
import os
from string import Template
try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser

from docopt import docopt


class Params:
    templatesDir = "_testTemplate"
    confFile = "config.conf"
    confSections = ["files"]
    fileCmake = "CMakeLists.txt"
    fileMain = "main.cpp"
    fileTest = "test.cpp"


def prepare_cmake():
    # find target_link_libraries, add modules
    # find FOLDER, add group

    pass


def prepare_main():
    pass


def prepare_test():
    pass


def border(func):
    def wrapper():
        print("####################################")
        func()
        print("####################################")
    return wrapper


@border
def read_config():
    config = ConfigParser()
    if not config.read("/".join([Params.templatesDir, Params.confFile])):
        print("can't read file %s" % "/".join([Params.templatesDir, Params.confFile]))
    else:
        print("Config:  %s" % config.items(Params.confSections[0]))


# main actions
if __name__ == '__main__':

    arguments = docopt(__doc__, argv="knCoreTest -g kncore --config conf --use kncore kngeo kngui ", version='0.1')

    # arguments = docopt(__doc__, version='0.1')

    # read_config()

    print(arguments)
    testName = arguments["TESTCASENAME"]
    modules = ", ".join(arguments["MODULE"])
    group = arguments["GROUP"]
    conf_file = arguments["FILE"]

    pwd = os.getcwd()

    out = Template("[$d] Create '$tnc' test in '$grp' group with modules '$mods' with config '$conf'.")
    print(Template.substitute(out, tnc=testName, grp=group, mods=modules, d=pwd, conf=Params.confFile))

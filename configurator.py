# from configparser import ConfigParser
from os.path import exists, dirname, realpath


class Params:
    templatesDir = "/".join([dirname(realpath(__file__)), "_testTemplate"])
    filenameCmake = "CMakeLists.txt"
    filenameMain = "main.cpp"
    filenameTest = "test.cpp"
    testDir = "test"
    testCaseName = "TestCaseName"
    testDirPostfix = "_test"

    class Config:
        section = "files"
        filename = "config.conf"

        @staticmethod
        def get_config_path():
            if exists(Params.Config.filename):
                return Params.Config.filename
            else:
                return ""

    @staticmethod
    def get_cmake_template():
        return "/".join([Params.templatesDir, Params.filenameCmake])

    @staticmethod
    def get_test_template():
        return "/".join([Params.templatesDir, Params.filenameTest])


# def read_config():
#     """Read configuration file and return params"""
#     config = ConfigParser()
#     if not config.read(Params.Config.filename):
#         print("can't read file %s" % Params.Config.get_config_path())
#     else:
#         print("Config: %s" % config.items(Params.Config.section))
#

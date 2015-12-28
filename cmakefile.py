import os
import ioworks as io
from configurator import Params

class CmakeFile:
    @staticmethod
    def prepare(path, group="", mods=[]):
        """ Change CMakeLists.txt file for new test """

        file_lines = io.get_lines(path)

        if mods.__len__() != 0 and group != "":
            for i in range(0, file_lines.__len__()):
                if file_lines[i].__contains__('target_link_libraries'):
                    module_str = " ".join(mods)
                    CmakeFile.append_modules(file_lines, i, module_str)
                if file_lines[i].__contains__('FOLDER'):
                    file_lines[i] = CmakeFile.change_folder(file_lines[i], group)
        return file_lines

    @staticmethod
    def change_folder(line, group):
        return line.replace('FOLDER "test"', 'FOLDER "test/%s"' % group)

    @staticmethod
    def append_modules(lines, i, modules_str):
        new_line = lines[i + 1].replace('testhelpers', modules_str)
        lines.insert(i + 1, new_line)

    @staticmethod
    def prepareParent(path, testDirName):
        return [testDirName.join(["add_subdirectory(",")\n"])]


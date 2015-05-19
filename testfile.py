import ioworks as io
from configurator import Params


class TestFile:

    @staticmethod
    def prepare(filepath, case_name):
        file_lines = io.get_lines(filepath)
        if case_name != "":
            for i in range(0, file_lines.__len__()):
                if file_lines[i].__contains__(Params.testCaseName):
                    file_lines[i] = file_lines[i].replace(Params.testCaseName, case_name)

        return file_lines

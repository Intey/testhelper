import ioworks as io


class TestFile:
    caseName = "TestCaseName"

    @staticmethod
    def prepare(filepath, case_name):
        file_lines = io.get_lines(filepath)
        if case_name != "":
            for i in range(0, file_lines.__len__()):
                if file_lines[i].__contains__(TestFile.caseName):
                    file_lines[i] = file_lines[i].replace(TestFile.caseName, case_name)

        return file_lines

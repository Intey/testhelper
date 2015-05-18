
def prepare(path, group="", mods=[]):
    """ Change CMakeLists.txt file for new test """

    file_lines = get_lines(path)

    if mods.__len__() != 0 and group != "":
        for i in range(0, file_lines.__len__()):
            try:
                if file_lines[i].__contains__('target_link_libraries'):
                    module_str = " ".join(mods)
                    append_modules(file_lines, i, module_str)

                if file_lines[i].__contains__('FOLDER'):
                    file_lines[i] = change_folder(file_lines[i], group)
            except:
                print(file_lines[i])
    return file_lines


def change_folder(line, group):
    return line.replace('FOLDER "test"', 'FOLDER "test/%s"' % group)


def append_modules(lines, i, modules_str):
    new_line = lines[i+1].replace('testhelpers', modules_str)
    lines.insert(i+1, new_line)

def get_lines(path):
    f = open(path, 'r')
    res = f.readlines()
    f.close()
    return res

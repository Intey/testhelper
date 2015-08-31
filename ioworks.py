def get_lines(path):
    """ read all lines in file
    :param path: filepath to read.
    :return: readed lines
    """
    f = open(path, 'r', encoding="UTF8")
    res = f.readlines()
    f.close()
    return res


def write_to_file(path, lines):
    file = open(path, 'w', encoding="UTF8")
    file.writelines(lines)
    file.close()
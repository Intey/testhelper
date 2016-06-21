def touch(path):
    open(path, 'a').close()
    return path

def get_lines(path):
    """ read all lines in file
    :param path: filepath to read.
    :return: readed lines
    """
    f = open(path, 'r')
    res = f.readlines()
    f.close()
    return res


def write_to_file(path, lines):
    file = open(path, 'w')
    file.writelines(lines)
    file.close()

def append_to_file(path, lines):
    file = open(path, 'a')
    file.writelines(lines)
    file.close()


def find_pos_in_file(path, regex):
    """Find line, where regex first time accure.
    :return: line number, where regex found in first time"""
    if regex == "":
        return 0
    import re
    f = open(path, 'r')
    for n,l in f:
        if re.match(regex, line):
            return n + 1 # inc, 'couze user count from 1, not 0
            break
    return 0
    f.close()

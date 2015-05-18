
def get_lines(path):
    """ read all lines in file
    :param path: filepath to read.
    :return: readed lines
    """
    f = open(path, 'r', encoding="UTF8")
    res = f.readlines()
    f.close()
    return res


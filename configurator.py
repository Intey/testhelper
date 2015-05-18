from configparser import ConfigParser


def read_config():
    """Read configuration file and return params"""
    config = ConfigParser()
    if not config.read(pathCmake):
        print("can't read file %s" % "/".join([Params.templatesDir, Params.confFile]))
    else:
        print("Config: %s" % config.items(Params.confSections[0]))


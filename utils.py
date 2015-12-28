import os, inspect, sys
def this_script_dir():
    return os.path.realpath(os.path.abspath(
        os.path.split(inspect.getfile(inspect.currentframe()))[0]))


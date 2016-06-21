import os
import shutil

class Assets:
    def __init__(self, folder):
        self._test_path = folder

    def up(self, fn):
        """Add 'assets' and 'tests' field to class, and create directory with
        cls.__name__. Skip, if directory exists."""
        def wrap(cls):
            cls.assets = os.path.join(self._test_path, cls.__name__, "assets")
            cls.temp   = os.path.join(self._test_path, cls.__name__, "temp")
            try:
                os.mkdir(cls.assets)
                os.mkdir(cls.temp)
            except OSError as e: pass
            fn(cls)

        return wrap


    def down(self, fn):
        """Remove directory, that represented in 'temp' field of class."""
        def wrap(cls):
            try:
                # shutil.rmtree(cls.assets)
                shutil.rmtree(cls.temp)
            except OSError as e:
                print("can't remove 'cls.temp'. You should use assetsUp decorator,"
                      + " on setUpClass.", e)
            fn(cls)

        return wrap


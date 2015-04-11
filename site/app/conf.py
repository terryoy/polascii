import sqlite3

# database session
def db():
    return sqlite3.connect('polascii.db', 
        detect_types=sqlite3.PARSE_DECLTYPES)

from ConfigParser import ConfigParser, NoOptionError
import traceback

class AppConfig:
    _config = None

    def __init__(self):
        self._config = ConfigParser()
        self._config.read('conf.ini')

    def get(self, key):
        return self._config.get('polascii-web', key)

conf = AppConfig()

__all__ = ['db', 'conf']



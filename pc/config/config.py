from ConfigParser import ConfigParser, NoOptionError
import os

class AppConfig(object):
	"""A general config loader for an application
	"""
	base_path = os.path.join(os.path.dirname(__file__), "../")

	def __init__(self, filename="config/conf.ini", section="config"):
		if not os.path.exists(filename):
			raise RuntimeError('application config file not found! please check: {0}'.format(filename))	

		self._config = ConfigParser()
		self._config.read(os.path.join(self.base_path, filename))

		self._defaultsection = section


	def get(self, option, section=None):
		get_section = section if section else self._defaultsection
		self._config.get(get_section, option)


polascii_config = AppConfig()

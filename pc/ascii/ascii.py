

class AsciiProcessor(object):
	"""Ascii interface for image to ascii conversion
	"""
	pass


class AAlibProcessor(AsciiProcessor):
	"""AsciiProcessor implemented with python-aalib
	"""
	pass

class CacaProcessor(AsciiProcessor):
	"""AsciiProcessor implemented with caca
	"""
	pass


class PolasciiAsciiProcessor(AsciiProcessor):
	"""Public facade for ascii processor with different implementation
	"""
	LIBAA = 1
	LIBCACA = 2

	_processor = None

	def __init__(self, impl='aa'):
		if impl == PolasciiAsciiProcessor.LIBAA or impl == 'aa':
			self._processor = AAlibProcessor()
		elif impl == PolasciiAsciiProcessor.LIBCACA or impl == 'caca':
			self._processor = CacaProcessor()
		else:
			raise RuntimeError("cannot initialize AsciiProcessor of implemenation: {0}".format(impl))




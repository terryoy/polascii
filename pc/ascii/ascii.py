

class AsciiProcessor(object):
	"""Ascii interface for image to ascii conversion
	"""

    def __init__(self, img):
        """
        The class handles one image's export per instance
        """
        self.image = img
        self.size = img.size
        
    def set_size(self, x, y):
        self.size = (x, y)

	def _export(self, path, format, **kwargs):
		raise NotImplementedError("You should call the sub class instead.")

    def export_txt(self, path, **kwargs):
        """
        Export the image in plain text format(aa_text_format) to the path specified
        """
        self._export(path, 'txt', **kwargs)

    def export_nhtml(self,path, **kwargs):
        """
        Export the image in Netscapeized HTML(aa_nhtml_format, with some level of grayscale)
        to the path speciied.
        """
        self._export(path, 'nhtml', **kwargs)

    def export_html(self, path, **kwargs):
        """
        Export the image in plain HTML (aa_html_format) to the path specified.
        """
        self._export(path, 'html', **kwargs)
        
    def export_more(self, path, **kawrgs):
        """
        Export the image in a more/less console format
        """
        self._export(path, 'more', **kwargs)

    def export_ansi(self, path, **kwargs):
        """
        Export the image in ansi ascii art
        """
        self._export(path, 'ansi', **kwargs)
        
    def export_irc(self, path, **kwargs):
        """
        Export the image in IRC escaped format
        """
        self._export(path, 'irc', **kwargs)




class AAlibProcessor(AsciiProcessor):
	"""AsciiProcessor implemented with python-aalib
	"""
	
	def __init__(self, img):
		from aalib_extra import export
		self._aalib_export = export

    def _export(self, path, format, **kwargs):
        if self.size != self.image.size:
            self._aalib_export(path, self.image.resize(self.size), format, **kwargs)
        else:
            self._aalib_export(path, self.image, format, **kwargs)


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




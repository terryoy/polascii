from aalib_extra import export

class PolasciiExport:
    
    _image = None
    _size = None

    def __init__(self, img):
        """
        The class handles one image's export per instance
        """
        self.image = img
        self.size = img.size
        
    def set_size(self, x, y):
        self.size = (x, y)
        
    def _export(self, path, format, **kwargs):
        if self.size != self.image.size:
            export(path, self.image.resize(self.size), format, **kwargs)
        else:
            export(path, self.image, format, **kwargs)

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





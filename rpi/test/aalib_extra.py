import aalib

aa_fastrender = aalib.libaa.aa_fastrender
aa_fastrender.argtypes = [aalib.ContextPtr] + 4 * [aalib.ctypes.c_int]


class AsciiScreenFast(aalib.AsciiScreen):

    def fastrender(self):
        '''Render the image(the fast way).
        
        no options.
   	'''
   	context = self._context
        buffer = aalib.aa_image(context)
        if buffer is None:
            raise NoImageBuffer
        width, height = self._render_width, self._render_height
        aa_fastrender(context, 0, 0, width, height)
        text = aalib.aa_text(context)
        attrs = aalib.aa_attrs(context)
        return [
            [
                (chr(text[y * width + x]), attrs[y * width + x])
                for x in xrange(width)
            ]
            for y in xrange(height)
        ]


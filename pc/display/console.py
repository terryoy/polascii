from ascii import aalib
import os, termios, sys, select, tty

class PolasciiConsole:

    screen = None
    contrast = 56   # 0..127
    brightness = 60  # 0..255
    _tty_settings = None

    def get_terminal_size(self, fd=1):
        """
        Returns height and width of current terminal. First tries to get
        size via termios.TIOCGWINSZ, then from environment. Defaults to 25
        lines x 80 columns if both methods fail.

        :param fd: file descriptor (default: 1=stdout)
        """
        try:
            import fcntl, termios, struct
            hw = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ, '1234'))
        except:
            try:
                hw = (os.environ['LINES'], os.environ['COLUMNS'])
            except:  
                hw = (25, 80)

        return hw

    def get_key(self):
        """
        Able to detect the key pressed in terminal in a non-blocking way
        """
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            key = sys.stdin.read(1)
            return key
        else:
            return None

    def __init__(self):
        height, width = self.get_terminal_size()
        self.screen = aalib.AsciiScreen(height=height, width=width)

        # init tty attributes
        self._tty_settings = termios.tcgetattr(sys.stdin)
        tty.setcbreak(sys.stdin.fileno())

    def __del__(self):
        termios.tcsetattr(sys.stdin, termios.TCSADRAIN, self._tty_settings)

    def display_image(self, img):
        self.screen.put_image((0,0), img.convert('L').resize(self.screen.virtual_size))
        print(self.screen.render(contrast=self.contrast, brightness=self.brightness))



if __name__ == '__main__':
    pass


# max7219.py
from micropython import const
import framebuf

# MAX7219 registers
_DIGIT0 = const(0x01)
_DECODEMODE = const(0x09)
_INTENSITY = const(0x0A)
_SCANLIMIT = const(0x0B)
_SHUTDOWN = const(0x0C)
_DISPLAYTEST = const(0x0F)

class Matrix8x8(framebuf.FrameBuffer):
    def __init__(self, spi, cs, num):
        self.spi = spi
        self.cs = cs
        self.cs.init(self.cs.OUT, value=1)
        self.num = num
        self.buffer = bytearray(8 * num)
        super().__init__(self.buffer, 8 * num, 8, framebuf.MONO_HLSB)
        self.init()

    def init(self):
        for cmd, data in (
            (_DISPLAYTEST, 0),
            (_SCANLIMIT, 7),
            (_DECODEMODE, 0),
            (_SHUTDOWN, 1),
        ):
            self._write(cmd, data)
        self.brightness(0)

    def brightness(self, value):
        if not 0 <= value <= 15:
            raise ValueError("Brightness out of range")
        self._write(_INTENSITY, value)

    def _write(self, command, data):
        self.cs(0)
        for _ in range(self.num):
            self.spi.write(bytearray([command, data]))
        self.cs(1)

    def show(self):
        for i in range(8):
            self.cs(0)
            for j in range(self.num):
                self.spi.write(
                    bytearray([_DIGIT0 + i, self.buffer[(j * 8) + i]])
                )
            self.cs(1)


import numpy as np
import png
from PIL import Image


class Bitmap:
    """
        RGB or ARGB bitmap array to set individual pixel in width X height pixel images.
    """

    def __init__(self, width, height, alpha=False):
        self.alpha = alpha
        self.width = width
        self.height = height
        if self.alpha:
            self._pixel_len = 4
        else:
            self._pixel_len = 3
        self.values = np.zeros((self._pixel_len * width * height), dtype=np.uint8)

    def clear(self, shade):
        self.values.fill(shade)

    def set_rgb_pixel(self, x, y, red, green, blue):
        index = (x + y * self.width) * self._pixel_len
        self.values[index] = red
        self.values[index + 1] = green
        self.values[index + 2] = blue

    def set_rgba_pixel(self, x, y, red, green, blue, alpha):
        index = (x + y * self.width) * self._pixel_len
        self.values[index] = red
        self.values[index + 1] = green
        self.values[index + 2] = blue
        self.values[index + 3] = alpha

    def copy_to_int_array(self):
        pass

    def copy_to_list_of_lists(self):
        return self.values.reshape(self.height, self.width * self._pixel_len)

    def save_as_png(self, file_path):
        mode = 'RGB'
        if self._pixel_len == 3:
            mode = 'RGB'
        if self._pixel_len == 4:
            mode = 'RGBA'
        png.from_array(self.copy_to_list_of_lists(), mode).save(file_path)

    def get_mode(self):
        if self._pixel_len == 3:
            return 'RGB'
        if self._pixel_len == 4:
            return 'RGBA'
        raise ValueError('Bitmap _pixel_len attribute error.')


class PilBitmap:
    """
        Use Pil Image under the hood.
        RGB or ARGB bitmap array to set individual pixel in width X height pixel images.
    """

    def __init__(self, width, height, alpha=False):
        self.alpha = alpha
        self.width = width
        self.height = height
        if self.alpha:
            self._pixel_len = 4
        else:
            self._pixel_len = 3
        self.im = Image.new(mode='RGBA', size=(self.width, self.height), color=(0, 0, 0, 255))

    def clear(self, shade):
        self.im = Image.new(mode='RGBA', size=(self.width, self.height), color=(shade, shade, shade, 255))

    def set_rgb_pixel(self, x, y, red, green, blue):
        self.im.putpixel((x, y), (red, green, blue, 255))

    def set_rgba_pixel(self, x, y, red, green, blue, alpha):
        self.im.putpixel((x, y), (red, green, blue, alpha))

    def copy_to_int_array(self):
        pass

    def copy_to_list_of_lists(self):
        return self.values.reshape(self.height, self.width * self._pixel_len)

    def save_as_png(self, file_path):
        self.im.save(file_path, 'PNG')

    def get_mode(self):
        if self._pixel_len == 3:
            return 'RGB'
        if self._pixel_len == 4:
            return 'RGBA'
        raise ValueError('PilBitmap _pixel_len attribute error.')

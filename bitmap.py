import numpy as np
import png


class Bitmap:
    """
        RGB or ARGB bitmap array to set individual pixel in width X height pixel images.
    """

    def __init__(self, width, height, alpha=False):
        self.alpha = alpha
        self.width = width
        self.height = height
        if self.alpha:
            self.pixel_len = 4
        else:
            self.pixel_len = 3
        self.values = np.zeros((self.pixel_len * width * height), dtype=np.uint8)

    def clear(self, shade):
        self.values.fill(shade)

    def set_rgb_pixel(self, x, y, red, green, blue):
        index = (x + y * self.width) * self.pixel_len
        self.values[index] = red
        self.values[index + 1] = green
        self.values[index + 2] = blue

    def set_rgba_pixel(self, x, y, red, green, blue, alpha):
        index = (x + y * self.width) * self.pixel_len
        self.values[index] = red
        self.values[index + 1] = green
        self.values[index + 2] = blue
        self.values[index + 3] = alpha

    def copy_to_int_array(self):
        pass

    def copy_to_list_of_lists(self):
        return self.values.reshape(self.height, self.width * self.pixel_len)

    def save_as_png(self, file_path):
        mode = 'RGB'
        if self.pixel_len == 3:
            mode = 'RGB'
        if self.pixel_len == 4:
            mode = 'RGBA'
        png.from_array(self.copy_to_list_of_lists(), mode).save(file_path)

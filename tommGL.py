import numpy as np
from math import floor

from bitmap import Bitmap


class Color:
    def __init__(self, r, g, b, a=None, data_type=np.uint8):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.data_type = data_type

    def has_alpha(self):
        if self.a is None:
            return False
        else:
            return True


def line(x0, y0, x1, y1, image: Bitmap, color):
    steep = False
    if abs(x0-x1) < abs(y0-y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = y1 - y0
    d_error = abs(dy)*2
    error = 0
    y = y0
    for x in range(x0, x1+1):
        if steep:
            image.set_rgb_pixel(y, x, color.r, color.g, color.b)
        else:
            image.set_rgb_pixel(x, y, color.r, color.g, color.b)
        error += d_error
        if error > dx:
            y += 1 if y1 > y0 else -1
            error -= dx * 2


def line_a(x0, y0, x1, y1, image: Bitmap, color):
    def plot(x, y, c):
        r = color.r * c
        g = color.g * c
        b = color.b * c
        image.set_rgb_pixel(int(x), int(y), int(r), int(g), int(b))

    def i_part(n):
        return floor(n)

    def rounded(n):
        return i_part(n + 0.5)

    def f_part(n):
        return n - floor(n)

    def rf_part(n):
        return 1 - f_part(n)

    steep = False
    if abs(x0 - x1) < abs(y0 - y1):
        x0, y0 = y0, x0
        x1, y1 = y1, x1
        steep = True
    if x0 > x1:
        x0, x1 = x1, x0
        y0, y1 = y1, y0
    dx = x1 - x0
    dy = y1 - y0
    gradient = dy / dx
    if dx == 0:
        gradient = 1

    x_end = round(x0)
    y_end = y0 + gradient * (x_end - x0)
    x_gap = rf_part(x0 + 0.5)
    x_pxl1 = x_end
    y_pxl1 = i_part(y_end)
    if steep:
        plot(y_pxl1, x_pxl1, rf_part(y_end) * x_gap)
        plot(y_pxl1 + 1, x_pxl1, f_part(y_end) * x_gap)
    else:
        plot(x_pxl1, y_pxl1, rf_part(y_end) * x_gap)
        plot(x_pxl1, y_pxl1 + 1, f_part(y_end) * x_gap)

    intery = y_end + gradient

    x_end = rounded(x1)
    y_end = y1 + gradient * (x_end - x1)
    x_gap = f_part(x1 + 0.5)
    x_pxl2 = x_end
    y_pxl2 = i_part(y_end)
    if steep:
        plot(y_pxl2, x_pxl2, rf_part(y_end) * x_gap)
        plot(y_pxl2 + 1, x_pxl2, f_part(y_end) * x_gap)
    else:
        plot(x_pxl2, y_pxl2, rf_part(y_end) * x_gap)
        plot(x_pxl2, y_pxl2 + 1, f_part(y_end) * x_gap)

    if steep:
        for _x in range(int(x_pxl1 + 1), int(x_pxl2)):
            plot(i_part(intery), _x, rf_part(intery))
            plot(i_part(intery) + 1, _x, f_part(intery))
            intery = intery + gradient
    else:
        for _x in range(int(x_pxl1 + 1), int(x_pxl2)):
            plot(_x, i_part(intery), rf_part(intery))
            plot(_x, i_part(intery) + 1, f_part(intery))
            intery = intery + gradient


def triangle_shape(x0, y0, x1, y1, x2, y2, image: Bitmap, color):
    line(x0, y0, x1, y1, image, color)
    line(x0, y0, x2, y2, image, color)
    line(x2, y2, x1, y1, image, color)


def triangle_a_shape(x0, y0, x1, y1, x2, y2, image: Bitmap, color):
    line_a(x0, y0, x1, y1, image, color)
    line_a(x0, y0, x2, y2, image, color)
    line_a(x2, y2, x1, y1, image, color)


if __name__ == "__main__":
    from timeit import default_timer as timer
    from datetime import datetime as dt

    h = 256
    w = 256
    im = Bitmap(w, h)

    line_a(10, 10, 150, 30, im, Color(255, 255, 0))
    line(10, 20, 150, 40, im, Color(255, 255, 0))
    triangle_shape(150, 150, 200, 80, 95, 123, im, Color(255, 255, 0))
    triangle_a_shape(120, 120, 170, 50, 65, 93, im, Color(255, 255, 0))

    path = "images/im_" + dt.now().strftime("%Y-%m-%d_%H:%M:%S") + ".png"
    print("Image saved: " + path)
    im.save_as_png(path)

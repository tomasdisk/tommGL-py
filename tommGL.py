import numpy as np
from timeit import default_timer as timer
from math import floor

from bitmap import Bitmap


class Color:
    def __init__(self, r, g, b, a=None, dtype=np.uint8):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self.dtype = dtype


def line(x0, y0, x1, y1, image:Bitmap, color):
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
    for x in range(x0, x1):
        if steep:
            image.set_rgb_pixel(y, x, color.r, color.g, color.b)
        else:
            image.set_rgb_pixel(x, y, color.r, color.g, color.b)
        error += d_error
        if error > dx:
            y += 1 if y1 > y0 else -1
            error -= dx * 2


def line_a(x0, y0, x1, y1, image:Bitmap, color):
    def plot(x, y, c):
        r = color.r * c
        g = color.g * c
        b = color.b * c
        image.set_rgb_pixel(int(x), int(y), int(r), int(g), int(b))

    def ipart(x):
        return floor(x)

    def round(x):
        return ipart(x + 0.5)

    def fpart(x):
        return x - floor(x)

    def rfpart(x):
        return 1 - fpart(x)

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

    xend = round(x0)
    yend = y0 + gradient * (xend - x0)
    xgap = rfpart(x0 + 0.5)
    xpxl1 = xend
    ypxl1 = ipart(yend)
    if steep:
        plot(ypxl1, xpxl1, rfpart(yend) * xgap)
        plot(ypxl1 + 1, xpxl1, fpart(yend) * xgap)
    else:
        plot(xpxl1, ypxl1, rfpart(yend) * xgap)
        plot(xpxl1, ypxl1 + 1, fpart(yend) * xgap)

    intery = yend + gradient

    xend = round(x1)
    yend = y1 + gradient * (xend - x1)
    xgap = fpart(x1 + 0.5)
    xpxl2 = xend
    ypxl2 = ipart(yend)
    if steep:
        plot(ypxl2, xpxl2, rfpart(yend) * xgap)
        plot(ypxl2 + 1, xpxl2, fpart(yend) * xgap)
    else:
        plot(xpxl2, ypxl2, rfpart(yend) * xgap)
        plot(xpxl2, ypxl2 + 1, fpart(yend) * xgap)

    if steep:
        for x in range(int(xpxl1 + 1), int(xpxl2)):
            plot(ipart(intery), x, rfpart(intery))
            plot(ipart(intery) + 1, x, fpart(intery))
            intery = intery + gradient
    else:
        for x in range(int(xpxl1 + 1), int(xpxl2)):
            plot(x, ipart(intery), rfpart(intery))
            plot(x, ipart(intery) + 1, fpart(intery))
            intery = intery + gradient


h = 256
w = 256
image = Bitmap(w, h)
line_a(10, 10, 150, 30, image, Color(255, 255, 255))
image.set_rgb_pixel(10, 10, 255, 0, 0)
image.set_rgb_pixel(150, 30, 255, 0, 0)

line(10, 20, 150, 40, image, Color(255, 255, 255))
image.set_rgb_pixel(10, 20, 255, 0, 0)
image.set_rgb_pixel(150, 40, 255, 0, 0)

path = "images/im_" + str(timer()) + ".png"
print("Image saved: " + path)
image.save_as_png(path)

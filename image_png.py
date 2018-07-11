import numpy as np
from datetime import datetime as dt
from timeit import default_timer as timer

from bitmap import Bitmap

h = 256
w = 256
image = Bitmap(w, h, alpha=True)

color_red = 0
for i in range(h):
    for j in range(w):
        image.set_rgba_pixel(j, i, color_red, 0, 0, 150)
    color_red += 1

path = "images/im_" + dt.now().strftime("%Y-%m-%d_%H:%M:%S") + ".png"
print("Image saved: " + path)
image.save_as_png(path)

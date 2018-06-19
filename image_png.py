import numpy as np
from timeit import default_timer as timer

from bitmap import Bitmap

h = 256
w = 256
image = Bitmap(w, h, alpha=True)

color_red = 255
color_green = 255
color_grey = 0
ran = 0
for i in range(h):
    for j in range(w):
        image.set_rgba_pixel(j, i, color_grey, color_grey - color_green + ran, 0, 150)
        # color_grey - color_red + ran
        color_grey += 1
        ran += 1
    ran = ran % np.random.randint(int(ran-ran*0.1), ran)
    color_red -= 1
    color_green -= 5
    color_green = color_green % 256


path = "images/im_" + str(timer()) + ".png"
print("Image saved: " + path)
image.save_as_png(path)

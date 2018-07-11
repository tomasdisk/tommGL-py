from datetime import datetime as dt
from bitmap import Bitmap, PilBitmap

h = 500
w = 500
image = Bitmap(w, h, alpha=True)
pil_image = PilBitmap(w, h, alpha=True)

color_red = 0
for i in range(h):
    for j in range(w):
        image.set_rgba_pixel(j, i, color_red, 0, 0, 150)
        pil_image.set_rgba_pixel(j, i, color_red, 0, 0, 150)
    color_red += 1

path = "images/im1_" + dt.now().strftime("%Y-%m-%d_%H:%M:%S") + ".png"
print("Image saved: " + path)
image.save_as_png(path)
path = "images/im2_" + dt.now().strftime("%Y-%m-%d_%H:%M:%S") + ".png"
print("Image saved: " + path)
pil_image.save_as_png(path)

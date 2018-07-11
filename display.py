import tkinter as tk
from PIL import Image, ImageTk
from math import sin, cos, radians
from timeit import default_timer as timer


def circle_cords(tetha):
    print(tetha)
    r = tetha // 10
    return int(cos(radians(tetha%360))*r), int(sin(radians(tetha%360))*r)


class StatusBar(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.label = tk.Label(self, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.label.pack(fill=tk.X)

    def set(self, text):
        self.label.config(text=text)
        self.label.update_idletasks()

    def clear(self):
        self.label.config(text="")
        self.label.update_idletasks()


class Display(tk.Frame):

    def __init__(self, parent, width=400, height=400, image: Image=None):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self._delta_time = timer()

        self.default_width = width
        self.default_height = height

        self._canvas = tk.Canvas(self.parent, width=width, height=height)
        self._canvas.pack()

        if image is None:
            self.image = Image.new(mode='RGBA', size=(width + 1, height + 1), color=(0, 0, 0, 255))
        else:
            self.image = image
        self._tk_image = ImageTk.PhotoImage(self.image)
        self._c_image = self._canvas.create_image(0, 0, anchor=tk.NW, image=self._tk_image)

        self.status_bar = StatusBar(self.parent)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # update handler
        # self.update_handler = None
        self.tetha = 0

        self.update_clock()

    def update_display(self, delta_time):
        # self.update_handler
        # r = self.tetha
        # g = 0
        # b = 0
        # if self.tetha > 255:
        #     r = 255
        #     g = self.tetha - 255
        #     if self.tetha > 510:
        #         r = 255
        #         g = 255
        #         b = self.tetha - 510
        #         if b == 255:
        #             self.tetha = 0
        #
        # color = (r, g, b)

        x, y = circle_cords(self.tetha)
        x += self.default_width // 2
        y += self.default_height // 2
        # aux = self.image.copy()
        aux = self.image
        aux.putpixel((x, y), (255, 255, 255, 255))
        self._tk_image = ImageTk.PhotoImage(aux.copy())
        self._canvas.itemconfigure(self._c_image, image=self._tk_image)
        self.status_bar.set("FPS: {:.5}".format(1 / delta_time))
        if self.tetha < 2514:
            self.tetha += 1
        else:
            self.image.save('images/im.png', 'PNG')
            self.tetha = 0

    def update_clock(self):
        delta_time = timer() - self._delta_time
        self.update_display(delta_time)
        self._delta_time = timer()
        self.parent.after(20, self.update_clock)


if __name__ == "__main__":
    w = 400
    h = 400
    # im.png = Image.new(mode='RGBA', size=(w + 1, h + 1), color=(255, 0, 0, 255))
    im = Image.open("images/im1_2018-07-11_11:43:01.png")
    w, h = im.size

    root = tk.Tk()
    Display(root, width=w, height=h, image=im).pack()
    root.mainloop()

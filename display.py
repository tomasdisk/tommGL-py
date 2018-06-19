import tkinter as tk


class Display(tk.Frame):
    def __init__(self, parent, width=400, height=400):
        tk.Frame.__init__(self, parent)
        self.default_width = width
        self.default_height = height
        self.canvas = tk.Canvas(parent, width=width, height=height)
        self.canvas.pack()


if __name__ == "__main__":
    root = tk.Tk()
    Display(root, width=400, height=400).pack()
    root.mainloop()

from itertools import cycle
import tkinter as tk
from PIL import ImageTk, Image

image_paths = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]

class Imagewindow(tk.Tk):
    def __init__(self, delay):
        tk.Tk.__init__(self)

        self.delay = delay
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()
        self.images = iter(image_paths)
        self.label = tk.Label(self, bd=0)
        self.label.pack()

    def slideShow(self):
        try:
            image_path = next(self.images)
        except StopIteration:
            return False

        img = Image.open(image_path)
        img.thumbnail((self.screen_width, self.screen_height), Image.ANTIALIAS)
        self.label.image = ImageTk.PhotoImage(img)
        self.label.config(image=self.label.image)
        self.after(self.delay*1000, self.slideShow)

    def run(self):
        self.mainloop()

def main():
    delay = 2

    root = Imagewindow(delay)
    root.overrideredirect(True)
    root.geometry('%dx%d+0+0' % (root.screen_width, root.screen_height))
    root.configure(background="black")
    root.focus_set()  # move focus to the the gui
    root.bind("<Escape>", lambda event: event.widget.quit())  # quit fullscreen with ESC
    root.slideShow()
    root.run()

if __name__ == "__main__":
    main()

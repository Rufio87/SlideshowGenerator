import tkinter as tk
from PIL import ImageTk, Image
import time

image_paths = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]

class Imagewindow(tk.Tk):
    def __init__(self, delay, transition):
        tk.Tk.__init__(self)

        self.transition = transition
        self.delay = delay
        self.screen_ratio = (self.winfo_screenwidth(), self.winfo_screenheight())
        self.images = iter(image_paths)
        self.label = tk.Label(self, bd=0)
        self.label.pack()

        self.alpha = 0
        self.current_image = None
        self.next_image = self.resize_image(next(self.images))

    def slideShow(self):
        try:
            image_path = next(self.images)
        except StopIteration:
            return False

        self.current_image = self.next_image
        self.next_image = self.resize_image(image_path)

        #blending images
        self.label.image = ImageTk.PhotoImage(self.current_image)
        self.label.config(image=self.label.image)

        self.after(self.delay*1000, self.fade_images)

    def fade_images(self):
        if self.alpha < 1.0:
            tmp_img = Image.blend(self.current_image, self.next_image, self.alpha)
            self.label.image = ImageTk.PhotoImage(tmp_img)
            self.label.config(image=self.label.image)
            self.alpha = self.alpha + 0.05
            self.after(200, self.fade_images)
        else:
            self.alpha = 0
            self.slideShow()

    def resize_image(self, image_path):
        img_temp = Image.open(image_path)
        #resize image to view in full screen
        img_temp.thumbnail(self.screen_ratio, Image.ANTIALIAS)
        #add black border to image such that each image has same size <- needed for blending images
        img_ratio = img_temp.size
        img = Image.new("RGB", self.screen_ratio)
        img.paste(img_temp, (int((self.screen_ratio[0]-img_ratio[0])/2),
                              int((self.screen_ratio[1]-img_ratio[1])/2)))
        return img

    def run(self):
        self.mainloop()

def main():
    delay = 2
    transition = True

    root = Imagewindow(delay, transition)
    root.overrideredirect(True)
    root.geometry('%dx%d+0+0' % (root.screen_ratio))
    root.configure(background="black")
    root.focus_set()  # move focus to the the gui
    root.bind("<Escape>", lambda event: event.widget.quit())  # quit fullscreen with ESC
    root.slideShow()
    root.run()

if __name__ == "__main__":
    main()

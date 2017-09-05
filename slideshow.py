import tkinter as tk
from PIL import ImageTk, Image
import time

image_paths = ["img1.jpg", "img2.jpg", "img3.jpg", "img4.jpg"]

class Imagewindow(tk.Tk):
    def __init__(self, delay, transition, alpha_step):
        tk.Tk.__init__(self)

        self.transition = transition
        self.delay = delay
        self.screen_ratio = (self.winfo_screenwidth(), self.winfo_screenheight())
        self.images = iter(image_paths)
        self.label = tk.Label(self, bd=0)
        self.label.pack()

        self.fade_these_images = None
        self.alpha_step = alpha_step
        self.current_image = None
        self.next_image = self.resize_image(next(self.images))

    def slideShow(self):
        try:
            image_path = next(self.images)
        except StopIteration:
            return
        self.current_image = self.next_image
        self.next_image = self.resize_image(image_path)

        #show image
        self.label.image = ImageTk.PhotoImage(self.current_image)
        self.label.config(image=self.label.image)
        #create blended images for fading
        self.fade_these_images = iter(self.create_fade_images(self.current_image, self.next_image, self.alpha_step))

        self.after(self.delay*1000, self.fade_images)

    def fade_images(self):
        try:
            self.label.config(image=next(self.fade_these_images))
            self.after(1, self.fade_images)
        except StopIteration:
            self.slideShow()

    def create_fade_images(self, current_image, next_image, alpha_step):
        fade_these_images = []
        alpha = 0
        while 1.0 >= alpha:
            tmp_img = Image.blend(current_image, next_image, alpha)
            fade_these_images.append(ImageTk.PhotoImage(tmp_img))
            alpha = alpha + alpha_step
        return fade_these_images

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
    alpha_step = 0.03

    root = Imagewindow(delay, transition, alpha_step)
    root.overrideredirect(True)
    root.geometry('%dx%d+0+0' % (root.screen_ratio))
    root.configure(background="black")
    root.focus_set()  # move focus to the the gui
    root.bind("<Escape>", lambda event: event.widget.quit())  # quit fullscreen with ESC
    root.slideShow()
    root.run()

if __name__ == "__main__":
    main()

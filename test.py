import tkinter as tk
from PIL import Image, ImageTk

test_img1 = "img1.jpg"
test_img2 = "img2.jpg"
test_img3 = "img3.jpg"

def get_screen_size(slideshow):
    return [slideshow.winfo_screenwidth(), slideshow.winfo_screenheight()]

def show_image(image_dir):
    slideshow = tk.Tk()
    canvas = tk.Canvas(slideshow, width=1224, height=1000)
    logo = tk.PhotoImage

def resize_image(img, screen_w, screen)

def main():
    #configure slideshow window
    slideshow = tk.Tk()
    [w, h] = get_screen_size(slideshow)  #get size of screen
    slideshow.overrideredirect(True)    #get rid of title bar and menu on the screen => full screen
    slideshow.geometry("%dx%d+0+0" % (w, h))
    slideshow.configure(background="black")
    slideshow.focus_set()  #move focus to the the gui
    slideshow.bind("<Escape>", lambda event: event.widget.quit())    #quit fullscreen with ESC


    #show image
    im = Image.open(test_img3)
    img = ImageTk.PhotoImage(im.resize([100,100]))
    label = tk.Label(slideshow, image=img, bd=0)
    label.pack()
    #start slideshow
    slideshow.mainloop()

if __name__ == "__main__":
    main()


#Image.Blend
from tkinter import *

def main():
    root = Tk()
    canvas = Canvas(root, width =1224,height=1000)
    logo=PhotoImage(file="17_03 Barcelona Marathon/DS_0339.jpg")
    canvas.create_image(0, 0, image=logo) #Change 0, 0 to whichever coordinates you need
    root.mainloop()

if __name__ == "__main__":
    main()
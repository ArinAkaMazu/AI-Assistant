from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
from pygame import mixer
mixer.init()
root = Tk()
root.attributes('-fullscreen', True)
def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    img = Image.open("giphy_s.gif")
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    mixer.music.load("bootsound.mp3")
    mixer.music.play()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    for img_frame in ImageSequence.Iterator(img):
        img_frame = img_frame.resize((screen_width, screen_height))
        img_frame = ImageTk.PhotoImage(img_frame)
        lbl.config(image=img_frame)
        root.update()
        time.sleep(0.05)
    root.destroy()
play_gif()
root.mainloop()

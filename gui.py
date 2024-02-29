from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
import requests
from io import BytesIO
from pygame import mixer

mixer.init()
root = Tk()
root.geometry("1000x500")


def play_gif():
    root.lift()
    root.attributes("-topmost", True)
    global img
    url = "https://media.giphy.com/media/doXBzUFJRxpaUbuaqz/giphy.gif"
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    for img_frame in ImageSequence.Iterator(img):
        img_frame = img_frame.resize((1000, 500))
        img_frame = ImageTk.PhotoImage(img_frame)
        lbl.config(image=img_frame)
        root.update()
        time.sleep(0.05)
    root.destroy()


play_gif()
root.mainloop()

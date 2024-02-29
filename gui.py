from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import time
from io import BytesIO
import requests
import pygame
from pygame import mixer
mixer.init()
root = Tk()
root.geometry("1000x500")
def play_gif(gif_url, music_file):
    root.lift()
    root.attributes("-topmost", True)
    global img
    response = requests.get(gif_url)
    img = Image.open(BytesIO(response.content))
    lbl = Label(root)
    lbl.place(x=0, y=0)
    i = 0
    mixer.music.load(music_file)
    mixer.music.play()
    for img_frame in ImageSequence.Iterator(img):
        img_frame = img_frame.resize((1000, 500))
        img_frame = ImageTk.PhotoImage(img_frame)
        lbl.config(image=img_frame)
        root.update()
        time.sleep(0.04)
    root.destroy()
gif_url = "https://media.giphy.com/media/doXBzUFJRxpaUbuaqz/giphy.gif"
music_file = "bootsound.mp3"  
play_gif(gif_url, music_file)
root.mainloop()

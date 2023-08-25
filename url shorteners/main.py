import pyshorteners
from tkinter import *

root = Tk()
root.geometry("350x100")
root.title("URL SHORTNER")




a = Label(root , text = "Enter Link").grid(row = 0 , column = 0)
b = Label(root , text = "Shortened URL").grid(row = 1 , column = 0)

url = Entry(root , width = 35)
url.grid(row = 0 , column = 1)

def short():
    f = url.get()
    shortlink = pyshorteners.Shortener().tinyurl.short(f)
    blank.insert(0, shortlink)


blank = Entry(root , width = 35)
blank.grid(row = 1 , column = 1)

b1 = Button(root , text = "Shorten Link" , command = short)
b1.grid(row = 4 , column = 1)

root.mainloop()
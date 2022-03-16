from PIL import Image, ImageFont, ImageDraw

import textwrap

def putText(result: object):
    text = result
    text = textwrap.fill(text=text, width=35)
    strip_width, strip_height = 1280, 800


    #my_image = Image.open("mountain1.jpg")
    #my_image = Image.open("water1.jpg")
    #my_image = Image.open("lake.jpg")
    my_image = Image.open("view.jpg")
    #my_image = Image.open("water1.jpg")



    title_font = ImageFont.truetype('Yagora.ttf', 60)

    draw = ImageDraw.Draw(my_image)

    text_width, text_height = draw.textsize(text, title_font)
    position = ((strip_width - text_width) / 2, (strip_height - text_height) / 2)

    draw.text(position, text=text, fill=(250, 250, 250), font=title_font)

    my_image.format = "PNG"

    my_image.show()

text = "Sample text for an on screen display"



# text = "my beautiful Cat, hello"
# para = textwrap.wrap(text, width=15)
#
# my_image = Image.open("background_blue.jpg")
#
# title_font = ImageFont.truetype('Yagora.ttf', 30)
#
# draw = ImageDraw.Draw(my_image)
#
# draw.text(xy=(200,200), text="my beautiful Cat", fill=(237, 230, 211), font=title_font)
#
# my_image.format = "PNG"
#
# my_image.show()


# from tkinter import *
#
# class login(Tk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("750x500")
#         #self.resizeable(False,False)
#     def Label(self):
#         self.backGroundImage=PhotoImage(file="blueblue.png")
#         self.backGroundImageLabel = Label(self, image=self.backGroundImage)
#         self.backGroundImageLabel.place(x=0,y=0)
#
#         self.cc=Label(self,text="My Message", font=('times', 24, 'italic'), highlightthickness=0)
#
#
#         self.cc.place(x=200,y=200)
#
#
#
#
# if __name__=="__main__":
#     Login=login()
#     Login.Label()
#     Login.mainloop()


#
# import tkinter as tk
# master = tk.Tk()
# whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
# msg = tk.Message(master, text = whatever_you_do)
# msg.config(bg='lightblue', font=('times', 24, 'italic'))
#
# msg.pack()
# tk.mainloop()
# root = Tk()
# root.geometry("300x200")
#
# w = Label(root, text='GeeksForGeeks', font="50")
# w.pack()
#
# msg = Message(root, text="A computer science portal for geeks")
#
# msg.pack()
#
# root.mainloop()
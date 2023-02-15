
import tkinter as tk

from constants.colors import *

def NewHomeBtn(master: tk.Canvas, command, text="Default", color='#F44336') -> tk.Button:
        return tk.Button(
            master=master, 
            text=text, 
            bg=color, 
            font=(HOME_BUTTON_FONT, 48, 'normal'), 
            fg='#ffffff',
            command=command,
            width=15,
            height=2
        )

def NewExitBtn(master: tk.Canvas, command, text="Default", color='#F44336') -> tk.Button:
        return tk.Button(
            master=master, 
            text=text, 
            bg=color, 
            font=(TEXT_FONT, 32, 'normal'), 
            fg='#ffffff',
            command=command,
        )

def NewMedBtn(master: tk.Canvas, command, text="Default", color='#F44336') -> tk.Button:
        return tk.Button(
            master=master, 
            text=text, 
            bg=color, 
            font=(TEXT_FONT, 48, 'normal'), 
            fg='#ffffff',
            command=command,
            height=1,
            width=15
        )

def evaText(canvas: tk.Canvas, text="Default", background=PRIMARY_COLOR, fg=TEXT_COLOR, font=TEXT_FONT) -> tk.Label:
        return tk.Label(
        master=canvas, 
        text=text, 
        background=background, 
        fg=TEXT_COLOR,
        font=(font, 32, 'normal')
    )

def evaFace(file: str="EXPOFILES/assets/evaFaceRedLarge.png", background: str=PRIMARY_COLOR):
    eva_face = tk.PhotoImage(file=file)
    eva_label = tk.Label(image=eva_face, width=eva_face.width(),height=eva_face.height(), background=background)
    eva_label.image = eva_face
    eva_label.pack()

    return eva_label

def clockText(root: tk.Tk, text="", font=("Roboto", 24), fg="black", bg=PRIMARY_COLOR):
    return tk.Label(root, text=text, font=font, fg=fg, bg=bg)

def newSettingsBtn(master: tk.Canvas, command, color='#F44336', font=TEXT_FONT) -> tk.Button:
        return tk.Button(
            master=master, 
            text="Settings", 
            bg=color, 
            font=(font, 55, 'normal'), 
            fg='#ffffff',
            command=command,
        )

import tkinter

def NewHomeBtn(master, command, text="Default", color='#F44336') -> tkinter.Button:
        return tkinter.Button(
            master=master, 
            text=text, 
            bg=color, 
            font=('arial', 55, 'normal'), 
            fg='#ffffff',
            command=command,
        )
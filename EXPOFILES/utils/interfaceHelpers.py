
import tkinter

def NewHomeBtn(master, command, text="Default") -> tkinter.Button:
        return tkinter.Button(
            master=master, 
            text=text, 
            bg='#F44336', 
            font=('arial', 55, 'normal'), 
            fg='#ffffff',
            command=command,
        )
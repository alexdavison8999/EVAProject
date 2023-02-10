
import tkinter

class HomeButton:
    def __init__(self, master, command, text="Default") -> None:
        tkinter.Button(
            master, 
            text=text, 
            bg='#F44336', 
            font=('arial', 55, 'normal'), 
            fg='#ffffff',
            command=command,
        )
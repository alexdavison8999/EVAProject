# PACKAGES
import tkinter as tk
from tkinter import messagebox
from time import strftime


# MODULES
from voiceRec import *
import confirmationGUI as confirmUI
from evaGUI import *
from postScanDisplay import *
from reportsGui import *
from drugInfoGui import *

WINDOW_HEIGHT=800
WINDOW_WIDTH=1280
BUTTON_PADDING=20


class EVAGUI:

    def __init__(self):

        self.root = tk.Tk()

        self.root.geometry("1280x800")
        self.root.title("Elderly Virtual Assistant")

        self.background_image = tk.PhotoImage(file='EXPOFILES/assets/view.png')
        self.evaFace = tk.PhotoImage(file="EXPOFILES/assets/evaFace4Home.png")

        self.my_canvas = tk.Canvas(self.root, width=1280, height=800)
        self.my_canvas.pack(fill="both", expand=True)

        self.my_canvas.create_image(
            0, 0, image=self.background_image, anchor="nw"
        )
        self.my_canvas.create_image(
            0, 0, image=self.evaFace, anchor="nw"
            )
        self.clock_text = tk.Label(
            self.root, text="", font=("Roboto", 50), fg="black"
        )

        self.clock_window = self.my_canvas.create_window(
            70, 530, anchor='nw', window=self.clock_text
        )

        self.evaText = "Hi I'm Eva.\nHow can I help you?"
        self.my_canvas.create_text(
            300, 250, text=self.evaText, font=("Roboto", 40), fill="black"
        )

        scan_btn = tk.Button(
            self.root, 
            text='Scan Bottle', 
            bg='#F44336', 
            font=('arial', 50, 'normal'), 
            fg='#ffffff',
            command=self.scanSelect
        )

        drug_info_btn = tk.Button(
            self.root, 
            text='Drug Info', 
            bg='#F44336', 
            font=('arial', 50, 'normal'),
            fg='#ffffff',
            command=self.drugInfoSelect
        )
        
        confirm_btn = tk.Button(
            self.root, 
            text='Daily Confirmation', 
            bg='#F44336', 
            font=('arial', 50, 'normal'),
            fg='#ffffff', 
            command=self.confirmSelect
        )
        
        report_btn = tk.Button(
            self.root, 
            text='Reports', 
            bg='#F44336', 
            font=('arial', 55, 'normal'), 
            fg='#ffffff',
            command=self.reportSelect
        )

        exit_btn = tk.Button(
            self.root, 
            text='Exit', 
            bg='#F44336', 
            font=('arial', 32, 'normal'), 
            fg='#ffffff',
            command=self.closeEVA,
        )
        # exit_btn = HomeButton(master=self.root, text='Exit', command=self.closeEVA)
        self.my_canvas.create_window(WINDOW_WIDTH,200,window=scan_btn, anchor=tk.E)
        self.my_canvas.create_window(WINDOW_WIDTH,300,window=drug_info_btn, anchor=tk.E)
        self.my_canvas.create_window(WINDOW_WIDTH,400,window=confirm_btn, anchor=tk.E)
        self.my_canvas.create_window(WINDOW_WIDTH,500,window=report_btn, anchor=tk.E)
        self.my_canvas.create_window(0 ,800,window=exit_btn, anchor=tk.SW)

        self.clock()
        self.root.mainloop()

    def scanSelect(self):
        print("Going to Bottle Scanning")
        loadingRamGui()
        displayFunct()

    def confirmSelect(self):
        print("Going to Medicine Confirmation")
        confirmUI.confirmGui()

    def reportSelect(self):
        print("Going to Reports")
        loadingReportGui()

    def drugInfoSelect(self):
        print("Going to Drug Info")
        loadingDrugGui()

    def closeEVA(self):
        if messagebox.askyesno(
            title="Exit EVA?", 
            message="Are you sure you want to exit?"
            ):
            self.root.destroy()
        else:
            print("Canceled exit request")

    def clock(self):
        time_string = strftime('%I:%M %p \n %A \n %B %d, %Y')
        self.clock_text.config(text= time_string)
        self.clock_text.after(1000,self.clock)
    
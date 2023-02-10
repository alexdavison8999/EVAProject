# PACKAGES
import tkinter as tk
from tkinter import messagebox
from time import strftime


# MODULES
from voiceRec import *
import confirmationGUI as confirmUI
import utils.interfaceHelpers as UI
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

        # Data Setup
        # This will be used to manage the UI elements on the canvas
        self.canvasIds = {}
        # Geometry for the application window size
        geometry = f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}'

        # print(geometry)

        # Root properties - these will remain consistent
        self.root.geometry(geometry)
        self.root.title("Elderly Virtual Assistant")
        # self.root.attributes('-fullscreen', True)
        
        # Main control for UI Elements
        self.canvas = tk.Canvas(self.root, width=1280, height=800)
        self.canvas.pack(fill="both", expand=True)

        # Initializing assets
        self.background_image = tk.PhotoImage(file='EXPOFILES/assets/view.png')
        self.eva_face = tk.PhotoImage(file="EXPOFILES/assets/evaFace4Home.png")

        # TODO: Maybe just rewrite this string depending on where we are rather than making new text to manage?
        self.eva_text = "Hi I'm Eva.\nHow can I help you?"
        self.clock_text = tk.Label(self.root, text="", font=("Roboto", 50), fg="black")

        # Program Navigation Buttons
        scan_btn = UI.NewHomeBtn(master=self.canvas, text='Scan Bottle', command=self.scanSelect)
        drug_info_btn = UI.NewHomeBtn(master=self.canvas, text='Drug Info', command=self.drugInfoSelect)
        confirm_btn = UI.NewHomeBtn(master=self.canvas, text='Daily Confirmation', command=self.confirmSelect)
        report_btn = UI.NewHomeBtn(master=self.canvas, text='Reports', command=self.reportSelect)
        exit_btn = UI.NewHomeBtn(master=self.canvas, text='Exit', command=self.closeEVA)

        # Adding assets to the canvas and the canvasIds list
        # These can be used to control the visibility of items
        self.canvasIds["Home"] = []
        self.canvasIds["Home"].append(self.canvas.create_image(
            0, 0, image=self.background_image, anchor="nw"
        ))
        self.canvasIds["Home"].append(self.canvas.create_image(
            0, 0, image=self.eva_face, anchor="nw"
            ))
        self.canvasIds["Home"].append(self.canvas.create_window(
            70, 530, anchor='nw', window=self.clock_text
        ))
        self.canvasIds["Home"].append(self.canvas.create_text(
            300, 250, text=self.eva_text, font=("Roboto", 40), fill="black"
        ))
        self.canvasIds["Home"].append(self.canvas.create_window(WINDOW_WIDTH,200,window=scan_btn, anchor=tk.E))
        self.canvasIds["Home"].append(self.canvas.create_window(WINDOW_WIDTH,300,window=drug_info_btn, anchor=tk.E))
        self.canvasIds["Home"].append(self.canvas.create_window(WINDOW_WIDTH,400,window=confirm_btn, anchor=tk.E))
        self.canvasIds["Home"].append(self.canvas.create_window(WINDOW_WIDTH,500,window=report_btn, anchor=tk.E))
        self.canvasIds["Home"].append(self.canvas.create_window(0 ,800,window=exit_btn, anchor=tk.SW))

        print(self.canvasIds["Home"])

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
        reportGui(self, self.canvas)

    def drugInfoSelect(self):
        print("Going to Drug Info")
        loadingDrugGui()

    def closeEVA(self):
        # self.root.withdraw()
        if messagebox.askyesno(
            title="Exit EVA?", 
            message="Are you sure you want to exit?"
            ):
            self.root.destroy()
        else:
            print("Canceled exit request")
            # self.root.deiconify()

    def clock(self):
        time_string = strftime('%I:%M %p \n %A \n %B %d, %Y')
        self.clock_text.config(text= time_string)
        self.clock_text.after(1000,self.clock)
    
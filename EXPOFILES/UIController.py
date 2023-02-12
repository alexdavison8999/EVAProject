from datetime import datetime
from time import strftime
import tkinter as tk
from tkinter import messagebox
import psycopg2.extensions


from homeGui import homeGui
from confirmationGUI import confirmGui
from drugInfoGui import loadingDrugGui
from reportsGui import reportGui
from evaGUI import loadingRamGui

from database.queries.query import timesList
from constants.window import *
from postScanDisplay import displayFunct

class UIController:
    """
    Class to handle UI for each screen and will contain core properties used
    throughout the code. This will perform asset cleanup and content management,
    as well as provide a DB connection at any point of the App
    Inputs:
        conn:       Postgresql connection object

    Arributes:


    """
    root: tk.Tk
    canvas: tk.Canvas
    conn: psycopg2.extensions.connection
    confirmList: dict
    canvasIds: dict
    geometry: str

    def __init__(self, conn: psycopg2.extensions.connection) -> None:
        self.root = tk.Tk()
        self.conn = conn
        self.confirmList = timesList(self.conn)
        # If these Id keys are changed, they must be updated on respective files
        self.canvasIds = {
            "Home": [],
            "Confirm": [],
            "Report": [],
            "DrugInfo": [],
            "ScanBottle": []
        }
        
        # Root properties - these will remain consistent
        self.root.geometry(f'{WINDOW_WIDTH}x{WINDOW_HEIGHT}')
        self.root.title("Elderly Virtual Assistant")
        # self.root.attributes('-fullscreen', True) # -- Look into using this instead

        # Canvas where all UI elements will be added to / removed from
        self.canvas = tk.Canvas(self.root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
        self.canvas.pack(fill="both", expand=True)

        self.clock_text = tk.Label(self.root, text="", font=("Roboto", 32), fg="black")

        # Load Home UI
        self.currentLocation = "Home"
        self.closeAndNavigateTo("Initialize", self.currentLocation)

        # Intitialize time based functionality
        self.clock()

        self.root.mainloop()

    def homeScreen(self):
        print("Loading Home Screen")
        homeGui(self)

    def scanSelect(self):
        print("Going to Bottle Scanning")
        loadingRamGui()
        displayFunct()

    def confirmSelect(self):
        print("Going to Medicine Confirmation")
        confirmGui(self)

    def reportSelect(self):
        print("Going to Reports")
        reportGui(self)

    def drugInfoSelect(self):
        print("Going to Drug Info")
        loadingDrugGui(self)

    def goToHome(self):
        self.closeAndNavigateTo(self.currentLocation, "Home")

    def goToDrugInfo(self):
        self.closeAndNavigateTo(self.currentLocation, "DrugInfo")

    def goToScan(self):
        self.closeAndNavigateTo(self.currentLocation, "Scan")

    def goToReport(self):
        self.closeAndNavigateTo(self.currentLocation, "Report")

    def goToConfirm(self):
        self.closeAndNavigateTo(self.currentLocation, "Confirm")

    def closeAndNavigateTo(self, curLocation: str, nextDesination: str) -> None:
        print(f"Going to {nextDesination} from {curLocation}")
        self.clearUI(curLocation)
        self.loadUI(nextDesination)

    def clearUI(self, canvasKey: str) -> None:
        if canvasKey == "Initialize":
            return
        try:
            [self.canvas.delete(itemId) for itemId in self.canvasIds[canvasKey]]
        except KeyError:
            print(f"ERROR: Cannot find canvas key {canvasKey} in dict keys {self.canvasIds.keys()}")
        return

    def loadUI(self, nextDestination) -> None:
        if nextDestination == "Home":
            self.currentLocation = "Home"
            self.homeScreen()
        elif nextDestination == "Report":
            self.currentLocation = "Report"
            self.reportSelect()
        elif nextDestination == "DrugInfo":
            self.currentLocation = "DrugInfo"
            self.drugInfoSelect()
        elif nextDestination == "Confirm":
            self.currentLocation = "Confirm"
            self.confirmSelect()
        else:
            self.currentLocation = "Home"
            self.scanSelect()

    def closeEVA(self):
        # root.withdraw()
        if messagebox.askyesno(
            title="Exit EVA?", 
            message="Are you sure you want to exit?"
            ):
            self.root.destroy()
        else:
            print("Canceled exit request")
            # root.deiconify()

    # Maybe split up code, need to see if it will affect the event loop
    def clock(self):
        time_string = strftime('%I:%M %p \n %A \n %B %d, %Y')
        date = datetime.now()

        # TODO: Create field for checking if the confirm has already been performed
        for key in self.confirmList:
            confirm = key
            hour_minute = confirm.split(':')
            print(f'HOUR: {date.strftime("%H")} MINUTE: {date.strftime("%M")} DATE: {hour_minute}')

            try:
                hour = hour_minute[0]
                minute = hour_minute[1]                
            except IndexError:
                print(f'Error getting hour minute split from entry {hour_minute} in list {UIController.confirmList}, time must be in a HH:MM format!')
                hour = -1
                minute = -1   

            if date.strftime("%H") == hour and date.strftime("%M") == minute:
                self.goToConfirm("Confirm")


        self.clock_text.config(text= time_string)
        self.clock_text.after(10000,self.clock)

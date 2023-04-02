from __future__ import annotations
import functools
import tkinter as tk
from typing import TYPE_CHECKING


from scanBottle.scanningFunction import scanningFunction
import utils.interfaceHelpers as UI

from constants.colors import *
from constants.window import *

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController

def goToCommand(UIController: UIController):
    print("Opening Camera Page")
    UIController.clearUI("ScanBottle")
    scanningFunction(UIController)
    return

def bottleScannerGui(UIController: UIController):

    # instructionPage = [
    #     [sg.Text('Instructions:', justification="center", font=('Calibri', 45))],
    #     [sg.Text('Capture images covering entire label of pill bottle', justification="center", font=('Calibri', 36))],
    #     [sg.Text('Hold the bottle closer to camera', justification="center", font=('Calibri', 36))],
    #     [sg.Text('Make sure there is proper lighting', justification="center", font=('Calibri', 36))],
    #     [sg.Button('Next', key='goToCameraPage')]
    # ]

    instructions_label = tk.Label(
        UIController.canvas, 
        text="Capture images covering entire label of pill bottle.\
             \nHold the bottle closer to camera.\nMake sure there is proper lighting.",
        font=(TEXT_FONT, 32, 'normal'),
        background=PRIMARY_COLOR,
        width=42,
        justify="left"
    )
    
    start_btn = UI.NewMedBtn(master=UIController.canvas, text='Add Bottle', command=functools.partial(goToCommand, UIController))
    go_back_btn = UI.NewExitBtn(master=UIController.canvas, text='Go Back', command=UIController.goToScanBottle)

    UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_PADDING, window=instructions_label, anchor=tk.N))
    UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT_PADDING, window=start_btn, anchor=tk.SE))
    UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW))
from __future__ import annotations
# PACKAGES
from datetime import datetime
import functools
import tkinter as tk
from time import strftime
from typing import TYPE_CHECKING

# MODULES
import utils.interfaceHelpers as UI
from evaGUI import *

from constants.window import *
from constants.colors import *


if TYPE_CHECKING:
    from UIController import UIController

img = None


def homeGui(UIController: UIController):
    """
    Class to handle UI for each screen and will contain core properties used
    throughout the code. This will perform asset cleanup and content management,
    as well as provide a DB connection at any point of the App
    
    Inputs:
        `UIController`:     UI Controller for the EVA App
    """
    # Another implementation of preventing garbage collection of assets
    # Will need to do this until there's a better way of arranging background images
    global background
    global eva_face
    # Initializing assets
    # background = tk.PhotoImage(file='EXPOFILES/assets/view.png')
    eva_face = tk.PhotoImage(file="EXPOFILES/assets/evaFaceRedLarge.png")

    # TODO: Maybe just rewrite this string depending on where we are rather than making new text to manage?
    eva_text = tk.Label(
        master=UIController.canvas, 
        text="Hi I'm Eva.\nHow can I help you?", 
        background=PRIMARY_COLOR, 
        fg=TEXT_COLOR,
        font=(TEXT_FONT, 32)
    )
    # eva_text.pack()

    date = datetime.now().strftime("%H %M")
    date = date.split(" ")
    print(date[0], date[1])

    # Program Navigation Buttons
    scan_btn = UI.NewHomeBtn(master=UIController.canvas, text='Scan Bottle', command=UIController.scanSelect)
    drug_info_btn = UI.NewHomeBtn(master=UIController.canvas, text='Drug Info', command=UIController.goToDrugInfo)
    confirm_btn = UI.NewHomeBtn(master=UIController.canvas, text='Daily Confirmation', command=functools.partial(UIController.goToConfirm, hour=date[0], minute=date[1]))
    report_btn = UI.NewHomeBtn(master=UIController.canvas, text='Reports', command=UIController.goToReport)
    exit_btn = UI.NewHomeBtn(master=UIController.canvas, text='Exit', command=UIController.closeEVA)

    # Adding assets to the canvas and the canvasIds list
    # These can be used to control the visibility of items
    # UIController.canvasIds["Home"].append(UIController.canvas.create_image(
    #     0, 0, image=background, anchor="nw"
    # ))
    UIController.canvasIds["Home"].append(UIController.canvas.create_image(
        300, WINDOW_HEIGHT / 2, image=eva_face
        ))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(
        WINDOW_WIDTH_PADDING, WINDOW_HEIGHT_PADDING, anchor='se', window=UIController.clock_text
    ))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(
        300, WINDOW_HEIGHT / 5, window=eva_text
    ))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,150,window=scan_btn, anchor=tk.E))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,300,window=drug_info_btn, anchor=tk.E))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,450,window=confirm_btn, anchor=tk.E))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,600,window=report_btn, anchor=tk.E))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_PADDING ,WINDOW_HEIGHT_PADDING,window=exit_btn, anchor=tk.SW))
    
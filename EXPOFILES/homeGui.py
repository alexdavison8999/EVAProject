from __future__ import annotations
# PACKAGES
import tkinter as tk
from time import strftime
from typing import TYPE_CHECKING

# MODULES
import utils.interfaceHelpers as UI
from evaGUI import *
from constants.window import *

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
    background = tk.PhotoImage(file='EXPOFILES/assets/view.png')
    eva_face = tk.PhotoImage(file="EXPOFILES/assets/evaFace4Home.png")

    # TODO: Maybe just rewrite this string depending on where we are rather than making new text to manage?
    eva_text = "Hi I'm Eva.\nHow can I help you?"

    # Program Navigation Buttons
    scan_btn = UI.NewHomeBtn(master=UIController.canvas, text='Scan Bottle', command=UIController.scanSelect)
    drug_info_btn = UI.NewHomeBtn(master=UIController.canvas, text='Drug Info', command=UIController.goToDrugInfo)
    confirm_btn = UI.NewHomeBtn(master=UIController.canvas, text='Daily Confirmation', command=UIController.goToConfirm)
    report_btn = UI.NewHomeBtn(master=UIController.canvas, text='Reports', command=UIController.goToReport)
    exit_btn = UI.NewHomeBtn(master=UIController.canvas, text='Exit', command=UIController.closeEVA)

    # Adding assets to the canvas and the canvasIds list
    # These can be used to control the visibility of items
    UIController.canvasIds["Home"].append(UIController.canvas.create_image(
        0, 0, image=background, anchor="nw"
    ))
    UIController.canvasIds["Home"].append(UIController.canvas.create_image(
        0, 0, image=eva_face, anchor="nw"
        ))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(
        70, 530, anchor='nw', window=UIController.clock_text
    ))
    UIController.canvasIds["Home"].append(UIController.canvas.create_text(
        300, 250, text=eva_text, font=("Roboto", 40), fill="black"
    ))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,200,window=scan_btn, anchor=tk.E))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,300,window=drug_info_btn, anchor=tk.E))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,400,window=confirm_btn, anchor=tk.E))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING,500,window=report_btn, anchor=tk.E))
    UIController.canvasIds["Home"].append(UIController.canvas.create_window(0 ,800,window=exit_btn, anchor=tk.SW))
    
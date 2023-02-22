from __future__ import annotations
import functools
import tkinter as tk
from typing import TYPE_CHECKING


from constants.colors import *
from constants.window import *
import utils.interfaceHelpers as UI

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController

def captureImage(UIController: UIController):
    print("Click!")
    return

def goToEdit(UIController: UIController):
    print("Going to med info edit")
    return

def goBack(UIController: UIController):
    print("Canceled")
    UIController.clearUI("ScanBottle")
    return 

def scanningFunction(UIController: UIController):

    # cameraPage = [
    #     [sg.Image(filename="", key="cam")],
    # ]

    # TODO: Make this dynamic
    num_photos = 0

    images_taken = tk.Label(master=UIController.canvas, text=f"Photos taken: {num_photos}", background=PRIMARY_COLOR)
    
    capture_img_btn = UI.NewExitBtn(master=UIController.canvas, text='Capture Image', command=functools.partial(captureImage, UIController))
    done_btn = UI.NewExitBtn(master=UIController.canvas, text='Done', command=functools.partial(goToEdit, UIController))
    cancel_btn = UI.NewExitBtn(master=UIController.canvas, text='Cancel', command=UIController.goToScanBottle)

    UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_PADDING, window=images_taken, anchor=tk.NW))
    UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT_PADDING, window=done_btn, anchor=tk.S))
    UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT_PADDING, window=capture_img_btn, anchor=tk.SE))
    UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=cancel_btn, anchor=tk.SW))
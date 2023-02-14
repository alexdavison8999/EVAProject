from __future__ import annotations
import functools
import tkinter as tk
from typing import TYPE_CHECKING


from constants.colors import *
from constants.window import *
import utils.interfaceHelpers as UI
from utils.itemHelpers import clearLocalUI

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController

def individualConfirm(UIController: UIController, medName: str, folderPath: str):

	# Creating a photoimage object to use image
	photo = tk.PhotoImage(file=r'%s' % "EXPOFILES/assets/image1.png")
	photo_label = tk.Label(image=photo, width=WINDOW_WIDTH / 2,height=WINDOW_HEIGHT / 2)
	photo_label.image = photo
	photo_label.pack()

	confirm_label = tk.Label(text=f'Have you taken your {medName}?', font=(TEXT_FONT, 55, 'normal'), background=PRIMARY_COLOR)

	no_btn = UI.NewExitBtn(master=UIController.canvas, text='No', color='#FF4040', command=UIController.goToHome)
	yes_btn = UI.NewExitBtn(master=UIController.canvas, text='Yes', color='#76EE00', command=UIController.goToHome)
	idk_btn = UI.NewExitBtn(master=UIController.canvas, text='IDK', color='#FFB90F',command=UIController.goToHome)

	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT / 2, window=photo_label, anchor=tk.W))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=confirm_label, anchor=tk.N))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 1.5, window=idk_btn, anchor=tk.E))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 2, window=no_btn, anchor=tk.E))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 3, window=yes_btn, anchor=tk.E))
from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING


from constants.window import *
from utils.itemHelpers import resetWindow
import utils.interfaceHelpers as UI

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController

# img = None

def confirmGui(UIController: UIController):

	# Creating a photoimage object to use image
	photo = tk.PhotoImage(file=r'%s' % "EXPOFILES/assets/image1.png")
	photo_label = tk.Label(image=photo, width=WINDOW_WIDTH / 2,height=WINDOW_HEIGHT / 2)
	photo_label.image = photo
	photo_label.pack()

	medicine = "Example Med"
	confirm_label = tk.Label(text=f'Have you taken your {medicine}?', font=('arial', 55, 'normal'))

	# photo1 = Image.open("C:\EVA\pillbottles\pillbottle1\Image1.png")
	#
	# photo1 = photo1._PhotoImage__photo.zoom(2)
	#
	#
	# photo = PhotoImage(photo1)

	no_btn = UI.NewHomeBtn(master=UIController.canvas, text='No', color='#FF4040', command=UIController.goToHome)
	yes_btn = UI.NewHomeBtn(master=UIController.canvas, text='Yes', color='#76EE00', command=UIController.goToHome)
	idk_btn = UI.NewHomeBtn(master=UIController.canvas, text='IDK', color='#FFB90F',command=UIController.goToHome)

	UIController.canvasIds["Confirm"] = []
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2, window=photo_label, anchor=tk.W))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=confirm_label, anchor=tk.N))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 1.5, window=idk_btn, anchor=tk.E))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 2, window=no_btn, anchor=tk.E))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 3, window=yes_btn, anchor=tk.E))
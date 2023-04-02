from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING
import functools
import voiceCommand

# from report2 import *
from reports.individualReport import individualReport
import utils.interfaceHelpers as UI
from database.queries.query import medicationsQuery

from constants.colors import *
from constants.window import *

if TYPE_CHECKING:
    from UIController import UIController

# Formulating Ideas from this thread: https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application
# Ideas from this could be useful later: https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
# https://www.tutorialspoint.com/how-to-clear-tkinter-canvas#:~:text=While%20creating%20a%20canvas%20in,present%20in%20a%20tkinter%20frame.

# Issues related to old tkinter bug that functions will not load image paths due to garbage collection
# https://stackoverflow.com/questions/16424091/why-does-tkinter-image-not-show-up-if-created-in-a-function

def goToCommand(UIController, medName):
	print("Click")
	individualReport(UIController, medName=medName)
	pass

# hides the home GUI and updates the canvas with the reports GUI
def reportGui(UIController: UIController) -> None:

	medications = medicationsQuery(UIController.conn)

	for index, med in enumerate(medications):
		med_button = UI.NewMedBtn(
			master=UIController.canvas, 
			text=f'{med.medName}', 
			command= functools.partial(goToCommand, UIController, med.medName)
		)
		yPos = (((index + 1) * 150) + (WINDOW_HEIGHT / 2))
		xPos = WINDOW_WIDTH / 1.35
		print(f'{index} {xPos}, {yPos}')
		med_button.grid(row=index, column=0)
		UIController.canvasIds["Report"].append(
			UIController.canvas.create_window(
				int(xPos),int(yPos), 
				window=med_button
			)
		)

	eva_face = UI.evaFace(file="EXPOFILES/assets/evaFaceRedLarge.png")
	microphone = tk.PhotoImage(file="EXPOFILES/assets/microphone.png")

	eva_text = UI.evaText(
		name="evaText",
        canvas=UIController.canvas, 
        text="Select a \nmedication report"
    )
	UIController.canvasIds["Report"].append(UIController.canvas.create_window(
        275, WINDOW_HEIGHT / 5, window=eva_text
    ))
	UIController.canvasIds["Report"].append(UIController.canvas.create_window(
        275, WINDOW_HEIGHT / 2, window=eva_face
    ))
	VC_btn = tk.Button(master=UIController.canvas, image=microphone, command=functools.partial(voiceCommand.record_speech, UIController, medications), bg="#F44336")
	VC_btn.image=microphone
	go_back_btn = UI.NewExitBtn(master=UIController.canvas, text='Go Back', command=UIController.goToHome)
	UIController.canvasIds["Report"].append(UIController.canvas.create_window(0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW))
	UIController.canvasIds["Report"].append(UIController.canvas.create_window(375,WINDOW_HEIGHT,window=VC_btn,anchor=tk.SW))
from __future__ import annotations
import functools
import tkinter as tk
from typing import TYPE_CHECKING
import voiceCommand

from confirmations.individualConfirm import individualConfirm
from constants.window import *
import utils.interfaceHelpers as UI
from utils.itemHelpers import clearLocalUI
from database.queries.query import medicationsQuery
from constants.colors import *

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController

# img = None

def goToCommand(UIController, medName, medId, filePath):
	UIController.clearUI("Confirm")
	print("Click")
	individualConfirm(UIController, medName=medName, medId=medId, filePath=filePath)
	pass

def goBack(UIController: UIController):
	# clearLocalUI(UIController.canvas, ui_ids)
	UIController.goToHome()

def confirmGui(UIController: UIController, hour: str='00', minute: str='00'):

	confirm_key = f'{hour}:{minute}'
	

	if confirm_key in UIController.confirmDict.keys():

		num_meds = len(UIController.confirmDict[confirm_key])
		confirm_label = tk.Label(text=f'You have {num_meds} medications', font=('arial', 55, 'normal'))

		for index, med in enumerate(UIController.confirmDict[confirm_key]):
			med_button = UI.NewMedBtn(
				master=UIController.canvas, 
				text=f'{med}', 
				command= functools.partial(goToCommand, UIController, med)
			)
			yPos = ((WINDOW_HEIGHT) - (((index + 1) * 150) + (WINDOW_HEIGHT / 2)))
			xPos = WINDOW_WIDTH / 1.35
			print(f'{index} {xPos}, {yPos}')
			med_button.grid(row=index, column=0)
			UIController.canvasIds["Confirm"].append(
				UIController.canvas.create_window(
					int(xPos),int(yPos), 
					window=med_button
				)
			)
		medications=UIController.confirmDict[confirm_key]
	else:
		print("Invalid key, returning all medications!")

		medications = medicationsQuery(UIController.conn)
		
		for index, med in enumerate(medications):
			med_button = UI.NewMedBtn(
				master=UIController.canvas, 
				text=f'{med.medName}', 
				command= functools.partial(goToCommand, UIController, med.medName, med.id, (med.folderPath + med.medName + '.png' ))
			)
			yPos = ((WINDOW_HEIGHT) - (((index + 1) * 150) + (WINDOW_HEIGHT / 2)))
			xPos = WINDOW_WIDTH / 1.35
			print(f'{index} {xPos}, {yPos}')
			med_button.grid(row=index, column=0)
			UIController.canvasIds["Confirm"].append(
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
        text=f"Select the \nmedicine to confirm \nfor {hour}:{minute}"
    )
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(
        275, WINDOW_HEIGHT / 5, window=eva_text
    ))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(
        275, WINDOW_HEIGHT / 2, window=eva_face
    ))

	VC_btn = tk.Button(master=UIController.canvas, image=microphone, command=functools.partial(voiceCommand.record_speech, UIController, medications), bg="#F44336")
	VC_btn.image=microphone
	go_back_btn = UI.NewExitBtn(master=UIController.canvas, text='Go Back', command=functools.partial(goBack, UIController))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(375,WINDOW_HEIGHT,window=VC_btn,anchor=tk.SW))
	# no_btn = UI.NewHomeBtn(master=UIController.canvas, text='No', color='#FF4040', command=UIController.goToHome)
	# yes_btn = UI.NewHomeBtn(master=UIController.canvas, text='Yes', color='#76EE00', command=UIController.goToHome)
	# idk_btn = UI.NewHomeBtn(master=UIController.canvas, text='IDK', color='#FFB90F',command=UIController.goToHome)

	# UIController.canvasIds["Confirm"] = []
	# UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH / 4, WINDOW_HEIGHT / 2, window=photo_label, anchor=tk.W))
	# UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=confirm_label, anchor=tk.N))
	# UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 1.5, window=idk_btn, anchor=tk.E))
	# UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 2, window=no_btn, anchor=tk.E))
	# UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 3, window=yes_btn, anchor=tk.E))
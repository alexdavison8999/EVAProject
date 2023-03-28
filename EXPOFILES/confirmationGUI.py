from __future__ import annotations
import functools
import os
import tkinter as tk
from typing import TYPE_CHECKING


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

def goToCommand(UIController, medName, medId):
	UIController.clearUI("Confirm")
	print("Click")
	individualConfirm(UIController, medName=medName, medId=medId)
	pass

def goBack(UIController: UIController):
	# clearLocalUI(UIController.canvas, ui_ids)
	UIController.goToHome()

def confirmGui(UIController: UIController, hour: str='00', minute: str='00'):

	confirm_key = f'{hour}:{minute}'
	

	if confirm_key in UIController.confirmDict.keys():

		num_meds = len(UIController.confirmDict[confirm_key])
		confirm_label = tk.Label(text=f'You have {num_meds} medications', font=('arial', 55, 'normal'))
  
		button_frame = tk.Frame(UIController.canvas, background=os.getenv("PRIMARY_COLOR"), border=1)
		button_frame.grid(row=0, column=0, sticky="e", rowspan=len(medications))
  
		# for index, med in enumerate(medications):
		# 	UI.NewMedBtn(
		# 		master=button_frame, 
		# 		text=f'{med.medName}', 
		# 		command= functools.partial(goToCommand, UIController, med.medName)
		# 	).grid(row=index, column=0)

		for index, med in enumerate(UIController.confirmDict[confirm_key]):
			UI.NewMedBtn(
				master=button_frame, 
				text=f'{med}', 
				command= functools.partial(goToCommand, UIController, med.medName, med.id)
			).grid(row=index, column=0, pady=GRID_PADDING)
			# yPos = ((WINDOW_HEIGHT) - (((index + 1) * 150) + (WINDOW_HEIGHT / 2)))
			# xPos = WINDOW_WIDTH / 1.35
			# print(f'{index} {xPos}, {yPos}')
			
	else:
		print("Invalid key, returning all medications!")

		medications = medicationsQuery(UIController.conn)
		button_frame = tk.Frame(UIController.canvas, background=os.getenv("PRIMARY_COLOR"), border=1)
		button_frame.grid(row=0, column=0, sticky="e", rowspan=len(medications))
  
		for index, med in enumerate(medications):
			UI.NewMedBtn(
				master=button_frame, 
				text=f'{med.medName}', 
				command= functools.partial(goToCommand, UIController, med.medName, med.id)
			).grid(row=index, column=0, pady=GRID_PADDING)
		
		# for index, med in enumerate(medications):
		# 	med_button = UI.NewMedBtn(
		# 		master=UIController.canvas, 
		# 		text=f'{med.medName}', 
		# 		command= functools.partial(goToCommand, UIController, med.medName, med.id)
		# 	)
		# 	yPos = ((WINDOW_HEIGHT) - (((index + 1) * 150) + (WINDOW_HEIGHT / 2)))
		# 	xPos = WINDOW_WIDTH / 1.35
		# 	print(f'{index} {xPos}, {yPos}')
		# 	med_button.grid(row=index, column=0)
		# 	UIController.canvasIds["Confirm"].append(
		# 		UIController.canvas.create_window(
		# 			int(xPos),int(yPos), 
		# 			window=med_button
		# 		)
		# 	)

	eva_face = UI.evaFace(file="EXPOFILES/assets/evaFaceRedLarge.png")

	eva_text = UI.evaText(
        canvas=UIController.canvas, 
        text=f"Select the \nmedicine to confirm \nfor {hour}:{minute}"
    )
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(
        275, WINDOW_HEIGHT / 5, window=eva_text
    ))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(
        275, WINDOW_HEIGHT / 2, window=eva_face
    ))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(
        WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 4, window=button_frame, anchor=tk.E
    ))

	go_back_btn = UI.NewExitBtn(master=UIController.canvas, text='Go Back', command=functools.partial(goBack, UIController))
	UIController.canvasIds["Confirm"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=go_back_btn, anchor=tk.SW))
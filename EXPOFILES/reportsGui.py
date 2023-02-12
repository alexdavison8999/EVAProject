from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING
import functools

# from report2 import *
from reports.individualReport import individualReport
import utils.interfaceHelpers as UI
from constants.window import *
from database.queries.query import medicationsQuery

if TYPE_CHECKING:
    from UIController import UIController

# Formulating Ideas from this thread: https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application
# Ideas from this could be useful later: https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
# https://www.tutorialspoint.com/how-to-clear-tkinter-canvas#:~:text=While%20creating%20a%20canvas%20in,present%20in%20a%20tkinter%20frame.

# Issues related to old tkinter bug that functions will not load image paths due to garbage collection
# https://stackoverflow.com/questions/16424091/why-does-tkinter-image-not-show-up-if-created-in-a-function

def goToCommand(UIController, medName):
	# loadingReportGui2()
	print("Click")
	individualReport(UIController, medName=medName)
	pass

# hides the home GUI and updates the canvas with the reports GUI
def reportGui(UIController: UIController) -> None:

	medications = medicationsQuery(UIController.conn)

	for index, med in enumerate(medications):
		med_button = UI.NewHomeBtn(
			master=UIController.canvas, 
			text=f'{med.medName}', 
			command= functools.partial(goToCommand, UIController, med.medName)
		)
		yPos = ((WINDOW_HEIGHT) - (((index + 1) * 150) + (WINDOW_HEIGHT / 2)))
		xPos = WINDOW_WIDTH / 1.35
		print(f'{index} {xPos}, {yPos}')
		med_button.grid(row=index, column=0)
		UIController.canvasIds["Report"].append(
			UIController.canvas.create_window(
				int(xPos),int(yPos), 
				window=med_button
			)
		)

	go_back_btn = UI.NewHomeBtn(master=UIController.canvas, text='Go Back', command=UIController.goToHome)
	UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=go_back_btn, anchor=tk.SW))

	

	# stats = getPercentConfirmsPerTimePeriod(UIController.conn, medName='med')

	# # This is the section of code which creates the a label
	# reports_label = tk.Label(UIController.canvas, text='Reports', bg='#F0F8FF', font=('arial', 40, 'normal'))

	# stats_label = tk.Label(UIController.canvas, text=f'{stats:.4g}% of confirmations\nreported as taken\nin the past week', bg='#F0F8FF', font=('arial', 24, 'normal'))

	# # Creating a photoimage object to use image
	# report_image = tk.PhotoImage(file="EXPOFILES/assets/report1.png")
	# report_label = tk.Label(image=report_image)
	# report_label.image = report_image

	# cog_report_btn = UI.NewHomeBtn(master=UIController.canvas, text='Cognitive Report', command=goToCommand)
	# go_back_btn = UI.NewHomeBtn(master=UIController.canvas, text='Go Back', command=UIController.goToHome)

	# # UIController.canvasIds["Report"] = []
	# UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=reports_label, anchor=tk.N))
	# UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT_PADDING, window=cog_report_btn, anchor=tk.SE))
	# UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=go_back_btn, anchor=tk.SW))
	# # UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_PADDING / 2, WINDOW_HEIGHT_PADDING / 2, window=click_me_btn))
	# UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, window=report_label, anchor=tk.CENTER))
	# UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_PADDING, window=stats_label, anchor=tk.NE))

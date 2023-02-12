from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

from report2 import *
import utils.interfaceHelpers as UI
from utils.itemHelpers import resetWindow
from constants.window import *
from database.queries.query import getPercentConfirmsPerTimePeriod

if TYPE_CHECKING:
    from UIController import UIController

# Formulating Ideas from this thread: https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application
# Ideas from this could be useful later: https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
# https://www.tutorialspoint.com/how-to-clear-tkinter-canvas#:~:text=While%20creating%20a%20canvas%20in,present%20in%20a%20tkinter%20frame.

# Issues related to old tkinter bug that functions will not load image paths due to garbage collection
# https://stackoverflow.com/questions/16424091/why-does-tkinter-image-not-show-up-if-created-in-a-function

def report2command():
	# loadingReportGui2()
	pass

# hides the home GUI and updates the canvas with the reports GUI
def reportGui(UIController: UIController) -> None:

	stats = getPercentConfirmsPerTimePeriod(UIController.conn, medName='med')

	# This is the section of code which creates the a label
	reports_label = tk.Label(UIController.canvas, text='Reports', bg='#F0F8FF', font=('arial', 40, 'normal'))

	stats_label = tk.Label(UIController.canvas, text=f'{stats:.4g}% of confirmations\nreported as taken\nin the past week', bg='#F0F8FF', font=('arial', 24, 'normal'))

	# Creating a photoimage object to use image
	report_image = tk.PhotoImage(file="EXPOFILES/assets/report1.png")
	report_label = tk.Label(image=report_image)
	report_label.image = report_image

	cog_report_btn = UI.NewHomeBtn(master=UIController.canvas, text='Cognitive Report', command=report2command)
	go_back_btn = UI.NewHomeBtn(master=UIController.canvas, text='Go Back', command=UIController.goToHome)

	UIController.canvasIds["Report"] = []
	UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=reports_label, anchor=tk.N))
	UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT_PADDING, window=cog_report_btn, anchor=tk.SE))
	UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=go_back_btn, anchor=tk.SW))
	# UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_PADDING / 2, WINDOW_HEIGHT_PADDING / 2, window=click_me_btn))
	UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, window=report_label, anchor=tk.CENTER))
	UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_PADDING, window=stats_label, anchor=tk.NE))

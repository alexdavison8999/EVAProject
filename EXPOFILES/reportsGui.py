import tkinter as tk

from report2 import *
import utils.interfaceHelpers as UI
from utils.itemHelpers import resetWindow
from constants.window import *
from database.queries.query import getPercentConfirmsPerTimePeriod

# Formulating Ideas from this thread: https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application
# Ideas from this could be useful later: https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
# https://www.tutorialspoint.com/how-to-clear-tkinter-canvas#:~:text=While%20creating%20a%20canvas%20in,present%20in%20a%20tkinter%20frame.

# Issues related to old tkinter bug that functions will not load image paths due to garbage collection
# https://stackoverflow.com/questions/16424091/why-does-tkinter-image-not-show-up-if-created-in-a-function

def report2command():
	# loadingReportGui2()
	pass

def clickFunc():
	print("Clicked!")

# hides the home GUI and updates the canvas with the reports GUI
def reportGui(GuiClass, classCanvas: tk.Canvas) -> None:

	# TODO: Figure out how to abstract this out of the upper function definition.
	# This is currently needed because I cannot figure out how to pass parameters
	# into the commands envoked by the buttons
	def cleanupReports() -> None:
		[classCanvas.delete(itemId) for itemId in GuiClass.canvasIds["Report"]]
		[classCanvas.itemconfig(itemId,state='normal') for itemId in GuiClass.canvasIds["Home"]]
		return

	# Hides all the current items in the canvas
	result = resetWindow(classCanvas, GuiClass.canvasIds,'Home')

	# If there are no issues hiding the previous page, then load reports page
	if result:

		stats = getPercentConfirmsPerTimePeriod(GuiClass.conn, medName='med')

		# This is the section of code which creates the a label
		reports_label = tk.Label(classCanvas, text='Reports', bg='#F0F8FF', font=('arial', 40, 'normal'))

		stats_label = tk.Label(classCanvas, text=f'{stats:.4g}% of confirmations\nreported as taken\nin the past week', bg='#F0F8FF', font=('arial', 24, 'normal'))

		# Creating a photoimage object to use image
		report_image = tk.PhotoImage(file="EXPOFILES/assets/report1.png")
		report_label = tk.Label(image=report_image)
		report_label.image = report_image

		cog_report_btn = UI.NewHomeBtn(master=classCanvas, text='Cognitive Report', command=report2command)
		go_back_btn = UI.NewHomeBtn(master=classCanvas, text='Go Back', command=cleanupReports)
		# click_me_btn = tk.Button(classCanvas, image=report_image, command=clickFunc)

		GuiClass.canvasIds["Report"] = []
		GuiClass.canvasIds["Report"].append(classCanvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=reports_label, anchor=tk.N))
		GuiClass.canvasIds["Report"].append(classCanvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT_PADDING, window=cog_report_btn, anchor=tk.SE))
		GuiClass.canvasIds["Report"].append(classCanvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=go_back_btn, anchor=tk.SW))
		# GuiClass.canvasIds["Report"].append(classCanvas.create_window(WINDOW_PADDING / 2, WINDOW_HEIGHT_PADDING / 2, window=click_me_btn))
		GuiClass.canvasIds["Report"].append(classCanvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, window=report_label, anchor=tk.CENTER))
		GuiClass.canvasIds["Report"].append(classCanvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_PADDING, window=stats_label, anchor=tk.NE))

	else:
		print("Error creating Report screen")
		return

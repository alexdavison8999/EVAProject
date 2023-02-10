import tkinter as tk

from report2 import *
import utils.interfaceHelpers as UI
from utils.itemHelpers import resetWindow
from constants.window import *

# Formulating Ideas from this thread: https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application
# Ideas from this could be useful later: https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
# https://www.tutorialspoint.com/how-to-clear-tkinter-canvas#:~:text=While%20creating%20a%20canvas%20in,present%20in%20a%20tkinter%20frame.

confir = 4

def report2command():
	# loadingReportGui2()
	pass

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

		# This is the section of code which creates the a label
		reports_label = tk.Label(classCanvas, text='Reports', bg='#F0F8FF', font=('arial', 40, 'normal'))

		# Creating a photoimage object to use image
		imPath = "EXPOFILES/assets/report1.png"
		photo = tk.PhotoImage(file=imPath)

		cog_report_btn = UI.NewHomeBtn(master=classCanvas, text='Cognitive Report', command=report2command)
		go_back_btn = UI.NewHomeBtn(master=classCanvas, text='Go Back', command=cleanupReports)
		click_me_btn = tk.Button(classCanvas, text='Click Me!', image=photo)

		GuiClass.canvasIds["Report"] = []
		GuiClass.canvasIds["Report"].append(GuiClass.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=reports_label, anchor=tk.N))
		GuiClass.canvasIds["Report"].append(GuiClass.canvas.create_window(WINDOW_WIDTH, WINDOW_HEIGHT, window=cog_report_btn, anchor=tk.SE))
		GuiClass.canvasIds["Report"].append(GuiClass.canvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=go_back_btn, anchor=tk.SW))
		# GuiClass.canvasIds["Report"].append(GuiClass.canvas.create_window(WINDOW_WIDTH / 4, 700, window=click_me_btn, anchor=tk.S))

	else:
		print("Error creating Report screen")
		return

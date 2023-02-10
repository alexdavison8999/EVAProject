import tkinter as tk

from report2 import *
import utils.interfaceHelpers as UI

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
		[classCanvas.delete(itemId) for itemId in GuiClass.canvasIds["report"]]
		[classCanvas.itemconfig(itemId,state='normal') for itemId in GuiClass.canvasIds["home"]]
		return

	# Hides all the current items in the canvas
	[classCanvas.itemconfig(itemId,state='hidden') for itemId in GuiClass.canvasIds["home"]]

	mat = tk.PhotoImage(file="EXPOFILES/assets/report1.png")
	# Adding widgets to the root window

	# This is the section of code which creates the a label
	label_1 = tk.Label(classCanvas, text='', bg='#F0F8FF', font=('arial', 40, 'normal'))

	# Creating a photoimage object to use image
	imPath = "EXPOFILES/assets/report1.png"
	photo = tk.PhotoImage(file=imPath)

	# .place(x=100, y=125)

	# This is the section of code which creates a button
	# .place(x=24, y=675)

	cog_report_btn = UI.NewHomeBtn(master=classCanvas, text='Cognitive report', command=report2command)
	go_back_btn = UI.NewHomeBtn(master=classCanvas, text='Go Back', command=cleanupReports)
	click_me_btn = tk.Button(classCanvas, text='Click Me!', image=photo)

	GuiClass.canvasIds["report"] = []
	GuiClass.canvasIds["report"].append(GuiClass.canvas.create_window(70, 530, window=label_1, anchor=tk.NW))
	GuiClass.canvasIds["report"].append(GuiClass.canvas.create_window(300, 125, window=cog_report_btn, anchor=tk.SW))
	GuiClass.canvasIds["report"].append(GuiClass.canvas.create_window(500, 675, window=go_back_btn, anchor=tk.SE))
	GuiClass.canvasIds["report"].append(GuiClass.canvas.create_window(1100, 640, window=click_me_btn, anchor=tk.S))

	# .place(x=1100, y=640)

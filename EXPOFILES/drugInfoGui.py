#specificDruginfo

import tkinter as tk
from tkinter import ttk
from tkinter import *
from utils.itemHelpers import resetWindow
from constants.window import *
import utils.interfaceHelpers as UI

import drugsCom as drugsCom

# TODO: Make the buttons dynamic to the data in the database. This should be 
# done by using a query to the database for all names in the database that aren't
# The unknown value and create a button for each one. Then, when a particular button
# is pressed, perform a web scrape for that medication

def loadingDrugGui(GuiClass, classCanvas: tk.Canvas):
	# TODO: Figure out how to abstract this out of the upper function definition.
	# This is currently needed because I cannot figure out how to pass parameters
	# into the commands envoked by the buttons
	def cleanupReports() -> None:
		[classCanvas.delete(itemId) for itemId in GuiClass.canvasIds["DrugInfo"]]
		[classCanvas.itemconfig(itemId,state='normal') for itemId in GuiClass.canvasIds["Home"]]
		return

	# Hides all the current items in the canvas
	result = resetWindow(classCanvas, GuiClass.canvasIds,'Home')

	# If there are no issues hiding the previous page, then load reports page
	if result:

		# This is the section of code which creates the a label
		reports_label = tk.Label(classCanvas, text='Drug Info', bg='#F0F8FF', font=('arial', 40, 'normal'))

		# Creating a photoimage object to use image
		times_asked = tk.PhotoImage(file="EXPOFILES/assets/timesAsked.png")
		label = Label(image=times_asked)
		label.image = times_asked

		rosuvastatin_btn = UI.NewHomeBtn(master=classCanvas, text='Rosuvastatin', command=drugsCom.rosuvastatin)
		tamsulosin_btn = UI.NewHomeBtn(master=classCanvas, text='Rosuvastatin', command=drugsCom.tamsulosin)
		go_back_btn = UI.NewHomeBtn(master=classCanvas, text='Go Back', command=cleanupReports)
		# click_me_btn = tk.Button(classCanvas, image=report_image, command=clickFunc)

		GuiClass.canvasIds["DrugInfo"] = []
		GuiClass.canvasIds["DrugInfo"].append(classCanvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=reports_label, anchor=tk.N))
		GuiClass.canvasIds["DrugInfo"].append(classCanvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT_PADDING, window=rosuvastatin_btn, anchor=tk.SE))
		GuiClass.canvasIds["DrugInfo"].append(classCanvas.create_window(WINDOW_WIDTH_PADDING / 2, WINDOW_HEIGHT_PADDING, window=tamsulosin_btn, anchor=tk.S))
		GuiClass.canvasIds["DrugInfo"].append(classCanvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=go_back_btn, anchor=tk.SW))
		# GuiClass.canvasIds["Report"].append(classCanvas.create_window(WINDOW_PADDING / 2, WINDOW_HEIGHT_PADDING / 2, window=click_me_btn))
		GuiClass.canvasIds["DrugInfo"].append(classCanvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, window=label, anchor=tk.CENTER))

	else:
		print("Error creating Drug Info screen")
		return
		
	# global root
	# root = Toplevel()

	# bg = PhotoImage(file="EXPOFILES/assets/view.png")

	# root.geometry('1280x800')

	# # Adding widgets to the root window

	# # This is the section of code which creates the a label
	# Label(root, text='Click Me !', image=bg).place(x=0, y=0)


	# # Creating a photoimage object to use image
	# imPath = "EXPOFILES/assets/timesAsked.png"
	# photo = PhotoImage(file=imPath)

	# print("oeo")

	# Button(root, text='Rosuvastatin', bg='#FFB90F', font=('Roboto', 40, 'normal'), command=rosuvastatin).place(x=200, y=200)

	# Button(root, text='Tamsulosin', bg='#E1912A', font=('Roboto', 40, 'normal'), command=tamsulosin).place(x=700, y=200)

	# Button(root, text='Exit', bg='#9A32CD', font=('Roboto', 40, 'normal'), command=btnClickFunction).place(x=1100, y=640)


	# if confir != 4:
	# 	return confir
	# print(confir)
	# print("imhere")

	# root.mainloop()


# path = "C:\EVA\pillbottles\pillbottle1\image1.png"
# loadingGui(path)

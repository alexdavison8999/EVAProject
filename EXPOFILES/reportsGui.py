import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

from report2 import *

# Formulating Ideas from this thread: https://stackoverflow.com/questions/14817210/using-buttons-in-tkinter-to-navigate-to-different-pages-of-the-application

confir = 4

def report2command():
	# loadingReportGui2()
	pass

def cleanupReports():
	pass


# creating tkinter window
# hides the home GUI and creates a canvas for the reports GUI
def reportGui(classRoot, classCanvas):

	classCanvas.itemconfig(1,state='hidden')

	# global root
	root = classRoot

	mat = PhotoImage(file="EXPOFILES/assets/report1.png")


	# Adding widgets to the root window

	# This is the section of code which creates the a label
	Label(root, text='', bg='#F0F8FF', font=('arial', 40, 'normal')).place(x=38, y=37)

	# Creating a photoimage object to use image
	imPath = "EXPOFILES/assets/report1.png"
	photo = PhotoImage(file=imPath)

	Button(root, text='Click Me !', image=photo).place(x=100, y=125)

	# This is the section of code which creates a button
	Button(root, text='Cognitive report', bg='#76EE00', font=('arial', 40, 'normal'), command=report2command(classRoot)).place(x=24, y=675)


	Button(root, text='Go Back', bg='#9A32CD', font=('arial', 40, 'normal'), command=cleanupReports).place(x=1100, y=640)

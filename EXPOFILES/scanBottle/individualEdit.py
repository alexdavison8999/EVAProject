from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING


from constants.colors import *
from database.queries.query import getMedByName
from postScanDisplay import funct2
from report2 import *
import utils.interfaceHelpers as UI
from constants.window import *

if TYPE_CHECKING:
    from UIController import UIController

def goToCorrectionPage(UIController: UIController, fieldToEdit: str):
    print("Going to corrections page!")
    return


def individualEdit(UIController: UIController, medName: str):

    if medName is not None:
        processedList = getMedByName(UIController.conn, medName)

    processedList = funct2()
    myIDVal = processedList[5][1]

    tk.Label(root, text=processedList[0][0], width=20, fg='Black', font=(TEXT_FONT, 16, 'bold')).grid(row=2, column=0)
    tk.Label(root, text=processedList[1][0], width=20, fg='Black', font=(TEXT_FONT, 16, 'bold')).grid(row=2, column=1)
    tk.Label(root, text=processedList[2][0], width=20, fg='Black', font=(TEXT_FONT, 16, 'bold')).grid(row=2, column=2)
    tk.Label(root, text=processedList[3][0], width=20, fg='Black', font=(TEXT_FONT, 16, 'bold')).grid(row=2, column=3)
    tk.Label(root, text=processedList[4][0], width=20, fg='Black', font=(TEXT_FONT, 16, 'bold')).grid(row=2, column=4)

    button1 = UI.NewMedBtn(root, text=processedList[0][1], width=20, fg='Black', font=(TEXT_FONT, 16, 'bold'),
                     command=lambda: goToCorrectionPage(UIController, "medName"))  # need to add command for actual button press
    button1.grid(row=3, column=0)

    button2 = UI.NewMedBtn(root, text=processedList[1][1], width=20, fg='Black', font=(TEXT_FONT, 16, 'bold'),
                     command=lambda: goToCorrectionPage(UIController, "refillsLeft"))
    button2.grid(row=3, column=1)

    button3 = UI.NewMedBtn(root, text=processedList[2][1], width=20, fg='Black', font=(TEXT_FONT, 16, 'bold'),
                     command=lambda: goToCorrectionPage(UIController, "timesPerWeek"))
    button3.grid(row=3, column=2)

    button4 = UI.NewMedBtn(root, text=processedList[3][1], width=20, fg='Black', font=(TEXT_FONT, 16, 'bold'),
                     command=lambda: goToCorrectionPage(UIController, "timesPerDay"))
    button4.grid(row=3, column=3)

    button5 = UI.NewMedBtn(root, text=processedList[4][1], width=20, fg='Black', font=(TEXT_FONT, 16, 'bold'),
                     command=lambda: goToCorrectionPage(UIController, "fieldToEdit"))
    button5.grid(row=3, column=4)

    root.mainloop()


    print("hereafter")
    root.quit()
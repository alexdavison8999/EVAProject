from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING
import functools
import voiceCommand
from database.classes.medications import Medication

# from report2 import *
from reports.individualReport import individualReport
import utils.interfaceHelpers as UI
from database.queries.query import medicationsQuery

from constants.colors import *
from constants.window import *

if TYPE_CHECKING:
    from UIController import UIController


def goToCommand(UIController: UIController, medication: Medication):
    print(f"Clicked {medication.medName}")
    UIController.individualInfoEdit(medication.medName)
    return


# hides the home GUI and updates the canvas with the reports GUI
def editBottleGui(UIController: UIController) -> None:
    medications = medicationsQuery(UIController.conn)

    for index, med in enumerate(medications):
        med_button = UI.NewMedBtn(
            master=UIController.canvas,
            text=f"{med.medName}",
            command=functools.partial(goToCommand, UIController, med),
        )
        yPos = ((index + 1) * 150) + (WINDOW_HEIGHT / 2)
        xPos = WINDOW_WIDTH / 1.35
        print(f"{index} {xPos}, {yPos}")
        med_button.grid(row=index, column=0)
        UIController.canvasIds["ScanBottle"].append(
            UIController.canvas.create_window(int(xPos), int(yPos), window=med_button)
        )

    eva_face = UI.evaFace(file="EXPOFILES/assets/evaFaceRedLarge.png")
    microphone = tk.PhotoImage(file="EXPOFILES/assets/microphone.png")

    eva_text = UI.evaText(
        name="evaText",
        canvas=UIController.canvas, text="Select a medication\nto edit"
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 5, window=eva_text)
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 2, window=eva_face)
    )

    VC_btn = tk.Button(master=UIController.canvas, image=microphone, command=functools.partial(voiceCommand.record_speech, UIController, medications), bg="#F44336")
    VC_btn.image=microphone
    UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(375,WINDOW_HEIGHT,window=VC_btn,anchor=tk.SW))
    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas, text="Go Back", command=UIController.goToHome
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW
        )
    )

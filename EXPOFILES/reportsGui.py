from __future__ import annotations
import os
import tkinter as tk
from typing import TYPE_CHECKING
import functools
import voiceCommand

# from report2 import *
from reports.individualReport import individualReport
import utils.interfaceHelpers as UI
from database.queries.query import medicationsQuery

from constants.colors import *
from constants.window import *

if TYPE_CHECKING:
    from UIController import UIController


def goToCommand(UIController, medName):
    print("Click")
    individualReport(UIController, medName=medName)
    pass


# hides the home GUI and updates the canvas with the reports GUI
def reportGui(UIController: UIController) -> None:
    medications = medicationsQuery(UIController.conn)
    button_frame = tk.Frame(
        UIController.canvas, background=os.getenv("PRIMARY_COLOR"), border=1
    )
    button_frame.grid(row=0, column=0, sticky="e", rowspan=len(medications))

    for index, med in enumerate(medications):
        UI.NewMedBtn(
            master=button_frame,
            text=f"{med.medName}",
            command=functools.partial(goToCommand, UIController, med.medName),
        ).grid(row=index, column=0, pady=GRID_PADDING)
        print(med.medName)
        print(index)

    eva_face = UI.evaFace(file="EXPOFILES/assets/evaFaceRedLarge.png")
    microphone = tk.PhotoImage(file="EXPOFILES/assets/microphone.png")
    VC_btn = tk.Button(
        master=UIController.canvas,
        image=microphone,
        command=functools.partial(
            voiceCommand.record_speech, UIController, medications
        ),
        bg="#F44336",
    )
    VC_btn.image = microphone

    eva_text = UI.evaText(
        name="evaText", canvas=UIController.canvas, text="Select a \nmedication report"
    )
    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas, text="Go Back", command=UIController.goToHome
    )

    UIController.canvasIds["Report"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 5, window=eva_text)
    )
    UIController.canvasIds["Report"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 2, window=eva_face)
    )
    UIController.canvasIds["Report"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 4, window=button_frame, anchor=tk.E
        )
    )
    UIController.canvasIds["Report"].append(
        UIController.canvas.create_window(
            375, WINDOW_HEIGHT, window=VC_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["Report"].append(
        UIController.canvas.create_window(
            0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW
        )
    )

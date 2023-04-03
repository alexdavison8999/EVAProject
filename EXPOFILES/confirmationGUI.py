from __future__ import annotations
import functools
import os
import tkinter as tk
from typing import TYPE_CHECKING
import voiceCommand

from confirmations.individualConfirm import individualConfirm
from constants.window import *
import utils.interfaceHelpers as UI
from utils.itemHelpers import clearLocalUI
from database.queries.query import medicationsQuery
from constants.colors import *

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController

# img = None


def goToCommand(UIController, medName, medId, filePath):
    UIController.clearUI("Confirm")
    print("Click")
    individualConfirm(UIController, medName=medName, medId=medId, filePath=filePath)
    pass


def goBack(UIController: UIController):
    # clearLocalUI(UIController.canvas, ui_ids)
    UIController.goToHome()


def confirmGui(UIController: UIController, hour: str = "00", minute: str = "00"):
    confirm_key = f"{hour}:{minute}"

    if confirm_key in UIController.confirmDict.keys():
        num_meds = len(UIController.confirmDict[confirm_key])
        confirm_label = tk.Label(
            text=f"You have {num_meds} medications", font=("arial", 55, "normal")
        )

        medications = UIController.confirmDict[confirm_key]

        button_frame = tk.Frame(
            UIController.canvas, background=os.getenv("PRIMARY_COLOR"), border=1
        )
        button_frame.grid(row=0, column=0, sticky="e", rowspan=len(medications))

        for index, med in enumerate(UIController.confirmDict[confirm_key]):
            UI.NewMedBtn(
                master=UIController.canvas,
                text=f"{med}",
                command=functools.partial(goToCommand, UIController, med),
            ).grid(row=index, column=0, pady=GRID_PADDING)

        medications = UIController.confirmDict[confirm_key]

    else:
        print("Returning all medications!")

        medications = medicationsQuery(UIController.conn)

        button_frame = tk.Frame(
            UIController.canvas, background=os.getenv("PRIMARY_COLOR"), border=1
        )
        button_frame.grid(row=0, column=0, sticky="e", rowspan=len(medications))

        for index, med in enumerate(medications):
            UI.NewMedBtn(
                master=button_frame,
                text=f"{med.medName}",
                command=functools.partial(
                    goToCommand,
                    UIController,
                    med.medName,
                    med.id,
                    (med.folderPath + med.medName + ".png"),
                ),
            ).grid(row=index, column=0, pady=GRID_PADDING)

    eva_face = UI.evaFace(file="EXPOFILES/assets/evaFaceRedLarge.png")
    microphone = tk.PhotoImage(file="EXPOFILES/assets/microphone.png")

    eva_text = UI.evaText(
        name="evaText",
        canvas=UIController.canvas,
        text=f"Select the \nmedicine to confirm \nfor {hour}:{minute}",
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 5, window=eva_text)
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 2, window=eva_face)
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 4, window=button_frame, anchor=tk.E
        )
    )

    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Go Back",
        command=functools.partial(goBack, UIController),
    )

    VC_btn = tk.Button(
        master=UIController.canvas,
        image=microphone,
        command=functools.partial(
            voiceCommand.record_speech, UIController, medications
        ),
        bg="#F44336",
    )
    VC_btn.image = microphone
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["Confirm"].append(
        UIController.canvas.create_window(
            375, WINDOW_HEIGHT, window=VC_btn, anchor=tk.SW
        )
    )

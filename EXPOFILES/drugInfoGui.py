from __future__ import annotations
import os
import tkinter as tk
from typing import TYPE_CHECKING

from drugInfo.individualDrug import individualDrug
import functools
import voiceCommand

from database.queries.query import medicationsQuery

from constants.window import *
import utils.interfaceHelpers as UI

if TYPE_CHECKING:
    from UIController import UIController


def goToCommand(UIController, medName):
    print("Click")
    individualDrug(UIController, medName=medName)
    return


def loadingDrugGui(UIController: UIController):
    # This is the section of code which creates the a label
    d_info_label = tk.Label(
        UIController.canvas,
        text="Drug Info",
        bg=os.getenv("PRIMARY_COLOR"),
        font=(os.getenv("TEXT_FONT"), 40, "normal"),
    )

    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas, text="Go Back", command=UIController.goToHome
    )

    UIController.canvasIds["DrugInfo"] = []

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

    eva_face = UI.evaFace(file="EXPOFILES/assets/evaFaceRedLarge.png")
    microphone = tk.PhotoImage(file="EXPOFILES/assets/microphone.png")
    eva_text = UI.evaText(
        name="evaText",
        canvas=UIController.canvas,
        text="Select a \nmed for information",
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 5, window=eva_text)
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(275, WINDOW_HEIGHT / 2, window=eva_face)
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING, WINDOW_HEIGHT / 3, window=button_frame, anchor=tk.E
        )
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

    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            375, WINDOW_HEIGHT, window=VC_btn, anchor=tk.SW
        )
    )

    UIController.canvasIds["DrugInfo"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=d_info_label, anchor=tk.N
        )
    )

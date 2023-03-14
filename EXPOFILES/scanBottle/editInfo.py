from __future__ import annotations
import os
import tkinter as tk
from typing import TYPE_CHECKING
from database.mutations.mutation import alterMedicine
from database.classes.medications import Medication
from scanBottle.counter import Counter
from scanBottle.keyboard import Keyboard


from constants.colors import *
import utils.interfaceHelpers as UI
from constants.window import *

if TYPE_CHECKING:
    from UIController import UIController


def confirmEdit(
    UIController: UIController,
    med: Medication,
    fieldToEdit: str,
    newVal: str,
    date_ids: list[Counter] = None,
):
    print(fieldToEdit, newVal)
    if fieldToEdit in ["refillDate", "dateFilled", "createdAt"]:
        date_list = []
        date_list.append(date_ids[4].get_value())
        date_list.append(date_ids[5].get_value())
        date_list.append(date_ids[6].get_value())
        date_list.append(date_ids[7].get_value())
        date_list.append(date_ids[0].get_value())
        date_list.append(date_ids[1].get_value())
        date_list.append(date_ids[2].get_value())
        date_list.append(date_ids[3].get_value())
        date_string = ""
        for index in range(len(date_list)):
            if index in [4, 6]:
                date_string = date_string + "-" + str(date_list[index])
            else:
                date_string = date_string + str(date_list[index])

        newVal = date_string
        print(date_string)

    result = alterMedicine(
        UIController.conn, med, fieldToEdit, newVal.replace("\n", "")
    )
    UIController.individualInfoEdit(med.medName, updateVal=result)


def goBack(UIController: UIController, medName):
    UIController.clearUI("ScanBottle")
    UIController.individualInfoEdit(medName)


def editInfo(
    UIController: UIController, med: Medication, fieldToEdit: str, curVal: str
):
    edit_text = fieldToEdit in ["medName"]
    date_field = fieldToEdit in ["refillDate", "dateFilled", "createdAt"]
    timesPerField = fieldToEdit in ["timesPerWeek", "timesPerDay"]
    date_ids = []

    if edit_text:
        keyboard_frame = Keyboard(UIController.canvas, curVal)
        confirm_button = UI.NewExitBtn(
            master=UIController.canvas,
            text="Save Changes",
            color=os.getenv("GREEN_COLOR"),
            command=lambda: confirmEdit(
                UIController, med, fieldToEdit, keyboard_frame.getValue()
            ),
        )
        UIController.canvasIds["ScanBottle"].append(
            UIController.canvas.create_window(
                WINDOW_PADDING, 0, window=keyboard_frame.text_widget, anchor=tk.NW
            )
        )
        UIController.canvasIds["ScanBottle"].append(
            UIController.canvas.create_window(
                WINDOW_WIDTH / 2,
                WINDOW_HEIGHT / 2,
                window=keyboard_frame.keyboard_frame,
                anchor=tk.CENTER,
            )
        )
    else:
        if date_field:
            for index in range(0, len(curVal)):
                if curVal[index] == "/":
                    forward_slash = tk.Label(
                        master=UIController.canvas,
                        text=curVal[index],
                        background=os.getenv("PRIMARY_COLOR"),
                        font=(os.getenv("TEXT_FONT"), 40),
                    )
                    UIController.canvasIds["ScanBottle"].append(
                        UIController.canvas.create_window(
                            ((index) * 125) + 75,
                            WINDOW_HEIGHT / 2,
                            window=forward_slash,
                            anchor=tk.CENTER,
                        )
                    )
                else:
                    if index == 0 or index == 3:
                        counter_frame = Counter(
                            UIController.canvas,
                            curVal[index],
                            upperLimit=1,
                            index=index,
                        )
                    elif index == 6:
                        counter_frame = Counter(
                            UIController.canvas,
                            curVal[index],
                            lowerLimit=1,
                            upperLimit=2,
                            index=index,
                        )
                    else:
                        counter_frame = Counter(
                            UIController.canvas, curVal[index], index=index
                        )
                    date_ids.append(counter_frame)
                    UIController.canvasIds["ScanBottle"].append(
                        UIController.canvas.create_window(
                            ((index) * 125) + 75,
                            WINDOW_HEIGHT / 2,
                            window=counter_frame.frame,
                            anchor=tk.CENTER,
                        )
                    )
            title_text = f"Edit the date for {fieldToEdit}"
        elif timesPerField:
            counter_frame = Counter(UIController.canvas, curVal)

            UIController.canvasIds["ScanBottle"].append(
                UIController.canvas.create_window(
                    WINDOW_WIDTH / 2,
                    WINDOW_HEIGHT / 2,
                    window=counter_frame.frame,
                    anchor=tk.CENTER,
                )
            )

            day_or_week = "day" if fieldToEdit == "timesPerDay" else "week"
            title_text = (
                f"Choose how many times per {day_or_week} you want to be notified."
            )
        else:
            for index in range(0, len(curVal)):
                counter_frame = Counter(UIController.canvas, curVal[index])
                UIController.canvasIds["ScanBottle"].append(
                    UIController.canvas.create_window(
                        ((index + 1) * 100) + 200,
                        WINDOW_HEIGHT / 2,
                        window=counter_frame.frame,
                        anchor=tk.CENTER,
                    )
                )
                title_text = f"Edit the field {fieldToEdit}"

        title_label = tk.Label(
            UIController.canvas,
            text=title_text,
            font=(TEXT_FONT, 28, "normal"),
            background=PRIMARY_COLOR,
        )
        confirm_button = UI.NewExitBtn(
            master=UIController.canvas,
            text="Save Changes",
            color=os.getenv("GREEN_COLOR"),
            command=lambda: confirmEdit(
                UIController,
                med,
                fieldToEdit,
                counter_frame.counter_text.get(),
                date_ids,
            ),
        )

        UIController.canvasIds["ScanBottle"].append(
            UIController.canvas.create_window(
                WINDOW_WIDTH / 2, WINDOW_PADDING, window=title_label, anchor=tk.N
            )
        )

    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Go Back",
        command=lambda: goBack(UIController, med.medName),
    )

    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            0, WINDOW_HEIGHT, window=go_back_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH, WINDOW_HEIGHT, window=confirm_button, anchor=tk.SE
        )
    )

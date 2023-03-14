from __future__ import annotations
import os
import tkinter as tk
from typing import TYPE_CHECKING, Union
from database.queries.query import getMedByName
from scanBottle.editInfo import editInfo
from database.classes.medications import Medication


from constants.colors import *
from report2 import *
import utils.interfaceHelpers as UI
from constants.window import *

if TYPE_CHECKING:
    from UIController import UIController


def camel_case_split(my_str: str):
    words = [[my_str[0]]]

    for c in my_str[1:]:
        if words[-1][-1].islower() and c.isupper():
            words.append(list(c))
        else:
            words[-1].append(c)

    string_arr = ["".join(word) for word in words]
    title_str = ""
    for str in string_arr:
        title_str = title_str + f"{str.capitalize()} "

    return title_str


def goToCorrectionPage(
    UIController: UIController, med: Medication, fieldToEdit: str, curVal: str
):
    print("Going to corrections page!")
    UIController.clearUI("ScanBottle")
    editInfo(UIController, med, fieldToEdit, curVal)
    return


def goBack(UIController: UIController):
    UIController.clearUI("ScanBottle")
    UIController.editBottleInfo()
    return


def list_to_string(day_list: list[str]):
    str_list = ""

    for index, day in enumerate(day_list):
        if index == 0:
            str_list += day
        elif index == 3:
            str_list += f"\n{day}"
        else:
            str_list += f", {day}"
    return str_list


def individualEdit(
    UIController: UIController, medName: str, update_val: Union[dict, None]
):
    med = getMedByName(UIController.conn, medName)

    title_text = tk.Label(
        UIController.canvas,
        text="Click on a button to edit the value",
        font=(TEXT_FONT, 32, "bold"),
        background=PRIMARY_COLOR,
    )

    if update_val:
        for item in update_val:
            title_string = camel_case_split(item)

            print(title_string)
            edited_text = tk.Label(
                UIController.canvas,
                text=f"{title_string}\nupdated to\n{update_val[item]}",
                font=(TEXT_FONT, 24, "bold"),
                background=os.getenv("LIGHT_GREEN")
                if title_string.lower() != "errors"
                else os.getenv("LIGHT_RED"),
            )
            # UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_WIDTH_PADDING, window=edited_text, anchor=tk.SW))

    label_frame = tk.Frame(UIController.canvas, background=os.getenv("PRIMARY_COLOR"))
    label_frame.grid(row=0, column=0, sticky="w")

    button_frame = tk.Frame(UIController.canvas, background=os.getenv("PRIMARY_COLOR"))
    button_frame.grid(row=0, column=0, sticky="w", rowspan=5)

    go_back_btn = UI.NewExitBtn(
        master=UIController.canvas, text="Go Back", command=lambda: goBack(UIController)
    )

    name_label = tk.Label(
        button_frame,
        text="Med Name",
        fg="Black",
        font=(TEXT_FONT, 16, "bold"),
        background=os.getenv("PRIMARY_COLOR"),
    )
    refills_label = tk.Label(
        button_frame,
        text="Refills Remaining",
        fg="Black",
        font=(TEXT_FONT, 16, "bold"),
        background=os.getenv("PRIMARY_COLOR"),
    )
    per_week_label = tk.Label(
        button_frame,
        text="Days Notified",
        fg="Black",
        font=(TEXT_FONT, 16, "bold"),
        background=os.getenv("PRIMARY_COLOR"),
    )
    per_day_label = tk.Label(
        button_frame,
        text="Times Notified",
        fg="Black",
        font=(TEXT_FONT, 16, "bold"),
        background=os.getenv("PRIMARY_COLOR"),
    )
    refill_date_label = tk.Label(
        button_frame,
        text="Refill Date",
        fg="Black",
        font=(TEXT_FONT, 16, "bold"),
        background=os.getenv("PRIMARY_COLOR"),
    )
    date_filled_label = tk.Label(
        button_frame,
        text="Date Filled",
        fg="Black",
        font=(TEXT_FONT, 16, "bold"),
        background=os.getenv("PRIMARY_COLOR"),
    )
    # date_added_label = tk.Label(button_frame, text="Date Added", fg='Black', font=(TEXT_FONT, 16, 'bold'), background=os.getenv('PRIMARY_COLOR'))
    # testing_label = tk.Label(button_frame, text="Testing", fg='Black', font=(TEXT_FONT, 16, 'bold'))

    name_label.grid(row=0, column=0, pady=GRID_PADDING)
    refills_label.grid(row=1, column=0, pady=GRID_PADDING)
    per_week_label.grid(row=2, column=0, pady=GRID_PADDING)
    per_day_label.grid(row=3, column=0, pady=GRID_PADDING)
    refill_date_label.grid(row=4, column=0, pady=GRID_PADDING)
    date_filled_label.grid(row=5, column=0, pady=GRID_PADDING)
    # date_added_label.grid(row=6, column=0, pady=GRID_PADDING)

    button1: tk.Button = tk.Button(
        button_frame,
        text=med.medName,
        width=30,
        height=2,
        fg="Black",
        font=(TEXT_FONT, 16, "bold"),
        command=lambda: goToCorrectionPage(UIController, med, "medName", med.medName),
    )
    button1.grid(row=0, column=1, pady=GRID_PADDING)

    button2 = tk.Button(
        button_frame,
        text=str(med.refillsLeft),
        width=30,
        height=2,
        font=(TEXT_FONT, 16, "bold"),
        command=lambda: goToCorrectionPage(
            UIController, med, "refillsLeft", str(med.refillsLeft)
        ),
    )
    button2.grid(row=1, column=1, pady=GRID_PADDING)

    days_string = list_to_string(med.timesPerWeek)

    button3 = tk.Button(
        button_frame,
        text=days_string,
        width=30,
        height=2,
        font=(TEXT_FONT, 16, "bold"),
        command=lambda: goToCorrectionPage(
            UIController, med, "timesPerWeek", days_string
        ),
    )
    button3.grid(row=2, column=1, pady=GRID_PADDING)

    button4 = tk.Button(
        button_frame,
        text=str(med.timesPerDay),
        width=30,
        height=2,
        font=(TEXT_FONT, 16, "bold"),
        command=lambda: goToCorrectionPage(
            UIController, med, "timesPerDay", str(med.timesPerDay)
        ),
    )
    button4.grid(row=3, column=1, pady=GRID_PADDING)

    button5 = tk.Button(
        button_frame,
        text=med.refillDate.strftime("%A, %B %d, %Y"),
        width=30,
        height=2,
        font=(TEXT_FONT, 16, "bold"),
        command=lambda: goToCorrectionPage(
            UIController, med, "refillDate", med.refillDate.strftime("%m/%d/%Y")
        ),
    )
    button5.grid(row=4, column=1, pady=GRID_PADDING)

    button6 = tk.Button(
        button_frame,
        text=med.dateFilled.strftime("%A, %B %d, %Y"),
        width=30,
        height=2,
        font=(TEXT_FONT, 16, "bold"),
        command=lambda: goToCorrectionPage(
            UIController, med, "dateFilled", med.dateFilled.strftime("%m/%d/%Y")
        ),
    )
    button6.grid(row=5, column=1, pady=GRID_PADDING)

    # button7 = tk.Button(
    #     button_frame,
    #     text=med.createdAt.strftime('%A, %B %d, %Y'),
    #     width=30,
    #     height=2,
    #     font=(TEXT_FONT, 16, 'bold'),
    #     command=lambda: goToCorrectionPage(UIController, med, "createdAt", med.createdAt.strftime("%m/%d/%Y"))
    # )
    # button7.grid(row=6, column=1, pady=GRID_PADDING)

    if update_val:
        UIController.canvasIds["ScanBottle"].append(
            UIController.canvas.create_window(
                WINDOW_PADDING + 200, WINDOW_HEIGHT / 2, window=edited_text, anchor=tk.E
            )
        )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=go_back_btn, anchor=tk.SW
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 1.8, WINDOW_HEIGHT / 2, window=button_frame, anchor=tk.CENTER
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_PADDING, window=title_text, anchor=tk.N
        )
    )
    # UIController.canvasIds["ScanBottle"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2.5, window=label_frame, anchor=tk.CENTER))
    return

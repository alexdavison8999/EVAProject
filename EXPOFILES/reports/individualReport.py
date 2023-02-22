from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

from report2 import *
import utils.interfaceHelpers as UI
from constants.window import *
from database.queries.query import getPercentConfirmsPerTimePeriod

if TYPE_CHECKING:
    from UIController import UIController
    
def individualReport(UIController: UIController, medName: str) -> None:

    def goBack():
        UIController.clearUI("Report")
        print(UIController.canvasIds)
        UIController.goToReport()

    UIController.clearUI("Report")

    stats = getPercentConfirmsPerTimePeriod(UIController.conn, medName)

    reports_label = tk.Label(UIController.canvas, text=f'Report for {medName}', bg='#F0F8FF', font=('arial', 40, 'normal'))
    stats_label = tk.Label(UIController.canvas, text=f'{stats:.4g}% of confirmations\nreported as taken\nin the past week', bg='#F0F8FF', font=('arial', 24, 'normal'))
    report_image = tk.PhotoImage(file="EXPOFILES/assets/report1.png")
    report_label = tk.Label(image=report_image)
    report_label.image = report_image
    cog_report_btn = UI.NewExitBtn(master=UIController.canvas, text='Cognitive Report', command=UIController.goToHome)
    go_back_btn = UI.NewExitBtn(master=UIController.canvas, text='Go Back', command=UIController.goToReport)
    UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_PADDING, window=reports_label, anchor=tk.NW))
    UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING, WINDOW_HEIGHT_PADDING, window=cog_report_btn, anchor=tk.SE))
    UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=go_back_btn, anchor=tk.SW))
    UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, window=report_label, anchor=tk.CENTER))
    UIController.canvasIds["Report"].append(UIController.canvas.create_window(WINDOW_WIDTH_PADDING + 20, WINDOW_PADDING - 20, window=stats_label, anchor=tk.NE))
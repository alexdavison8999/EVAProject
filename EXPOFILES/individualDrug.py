from __future__ import annotations
import tkinter as tk
from typing import TYPE_CHECKING

import requests
from bs4 import BeautifulSoup
import utils.interfaceHelpers as UI
from constants.window import *

whatis = "What is"
warningString = "Warning"
seString = 'side effects'
iTakeString = 'take'

if TYPE_CHECKING:
    from UIController import UIController

def readSite(url, drugname):
    resp = requests.get(url)
    infoCount = 0

    if resp.status_code == 200:

        soup = BeautifulSoup(resp.text, 'lxml')

        for data in soup.find_all('h2'):
            if whatis in data.text:
                for dat in data.find_all_next(['p', 'h2']):
                    if infoCount > 0:
                        break
                    if dat.name == 'h2':
                        break
                    print(dat.text)
                    return dat.text
                    infoCount = infoCount + 1
        return soup
    else:
        print('couldnt open')

def individualDrug(UIController: UIController, medName: str) -> None:

    def goBack():
        UIController.clearUI("DrugInfo")
        print(UIController.canvasIds)
        UIController.goToDrugInfo()

    UIController.clearUI("DrugInfo")

    url = f'https://www.drugs.com/{medName}.html'
    siteText = readSite(url, medName)
    
    info_label = tk.Label(UIController.canvas, text=f'{medName}', bg='#F0F8FF', font=('arial', 40, 'normal'))
    info_text = tk.Label(UIController.canvas, text=f'{siteText}', bg='#F0F8FF', font=('arial', 20, 'normal'), wraplength=1000)
    go_back_btn = UI.NewExitBtn(master=UIController.canvas, text='Go Back', command=UIController.goToDrugInfo)

    UIController.canvasIds["DrugInfo"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 20, window=info_label, anchor=tk.N))
    UIController.canvasIds["DrugInfo"].append(UIController.canvas.create_window(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, window=info_text, anchor=tk.CENTER))
    UIController.canvasIds["DrugInfo"].append(UIController.canvas.create_window(WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=go_back_btn, anchor=tk.SW))

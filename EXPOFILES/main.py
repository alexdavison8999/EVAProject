import tkinter as tk
from UIController import UIController
from constants.window import *
from database.dbUtils import connectToEvaDB
import GUI 

def main():
    app_conn = connectToEvaDB()
    myUIController = UIController(app_conn)

    # myApp = GUI.EVAGUI(app_root, app_conn)

    # myUIController.closeAndNavigateTo("Initialize", "Home")


if __name__ == '__main__':
    main()
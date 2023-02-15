import tkinter as tk
import firebase_admin

from UIController import UIController
from constants.window import *
from database.dbUtils import connectToEvaDB


def main():
    app_conn = connectToEvaDB()
    default_app = firebase_admin.initialize_app()
    myUIController = UIController(app_conn)

    # myApp = GUI.EVAGUI(app_root, app_conn)

    # myUIController.closeAndNavigateTo("Initialize", "Home")


if __name__ == '__main__':
    main()
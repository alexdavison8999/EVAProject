import tkinter as tk
from database.dbUtils import connectToEvaDB
import GUI 

def main():
    app_root = tk.Tk()
    app_conn = connectToEvaDB()
    myApp = GUI.EVAGUI(app_root, app_conn)
    return


if __name__ == '__main__':
    main()
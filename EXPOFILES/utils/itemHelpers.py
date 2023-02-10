import tkinter as tk
from typing import Literal

# from utils.appLocation import AppLocation

APP_LOCATIONS = ['Home', 'Drug Info', 'Report', 'Confirm']

# Function to delete all the UI from the canvas given a specific location
# Returns False if the given app location is not in the list above
def resetWindow(canvas: tk.Canvas, canvasIds: list[int],appLocation: str) -> bool:
    if appLocation not in APP_LOCATIONS:
        print(f"ERROR: App location {appLocation} not present in {APP_LOCATIONS}!")
        return False
    else:
        [canvas.itemconfig(itemId,state='hidden') for itemId in canvasIds[appLocation]]
        return True
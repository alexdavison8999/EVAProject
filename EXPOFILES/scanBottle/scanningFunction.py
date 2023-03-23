from __future__ import annotations
import functools
import tkinter as tk
from typing import TYPE_CHECKING


from utils.wrappers import on_rpi
from scanBottle.camera.cameraControls import CV2Camera, Camera
from constants.colors import *
from constants.window import *
import utils.interfaceHelpers as UI

# this is the function called when the button is clicked

if TYPE_CHECKING:
    from UIController import UIController


def captureImage(UIController: UIController):
    label: tk.Label = UIController.canvas.nametowidget("!labelNumPhotos")
    print(label["text"])
    num_photos = int(label["text"][-1])
    num_photos += 1
    print(num_photos)
    label.config(text=f"Photos taken: {num_photos}")
    print("Click!")
    return


def goToEdit(UIController: UIController):
    print("Going to med info edit")
    return


def goBack(UIController: UIController):
    print("Canceled")
    UIController.clearUI("ScanBottle")
    return


def scanningFunction(UIController: UIController):
    images_taken = tk.Label(
        master=UIController.canvas,
        name="!labelNumPhotos",
        text=f"Photos taken: 0",
        background=PRIMARY_COLOR,
    )

    # Check if we're on the raspberry pi or not
    if on_rpi():
        # camera: Camera = UIController.start_camera()

        # UIController.run_camera(camera)
        camera = CV2Camera()
        UIController.canvasIds["ScanBottle"].append(
            UIController.canvas.create_window(
                WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, window=camera.label, anchor=tk.NW
            )
        )

    capture_img_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Capture Image",
        command=functools.partial(captureImage, UIController),
    )
    done_btn = UI.NewExitBtn(
        master=UIController.canvas,
        text="Done",
        command=functools.partial(goToEdit, UIController),
    )
    cancel_btn = UI.NewExitBtn(
        master=UIController.canvas, text="Cancel", command=UIController.goToScanBottle
    )

    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_PADDING, window=images_taken, anchor=tk.NW
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH / 2, WINDOW_HEIGHT_PADDING, window=done_btn, anchor=tk.S
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_WIDTH_PADDING,
            WINDOW_HEIGHT_PADDING,
            window=capture_img_btn,
            anchor=tk.SE,
        )
    )
    UIController.canvasIds["ScanBottle"].append(
        UIController.canvas.create_window(
            WINDOW_PADDING, WINDOW_HEIGHT_PADDING, window=cancel_btn, anchor=tk.SW
        )
    )

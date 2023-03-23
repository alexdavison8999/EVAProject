import os
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import io

import cv2


class Camera:  # Originally a tk object, some stuff may reflect that
    """
    Class for the Camera, place the label in the scene to get the feed on screen
    """

    def __init__(self, root):
        # Set up the camera feed
        cmd = ["raspistill", "-t", "0", "-w", "640", "-h", "480", "-o", "-"]
        self.p = subprocess.Popen(cmd, stdout=subprocess.PIPE, preexec_fn=os.setsid)
        self.stream = io.BytesIO(self.p.stdout.read())

        # self.test_image = tk.Label(root)
        # photo = ImageTk.PhotoImage("EXPOFILES/assets/image1.png")
        # self.test_image.config(image=photo)
        # self.test_image.image = photo

        # Create a label to display the camera feed
        self.label = tk.Label(root)
        self.label.pack()

        # Continuously update the camera feed on the label
        self.photo = None
        self.update_feed(self.stream)

    def update_feed(self, stream):
        # Read the next image from the stream
        stream.seek(0)
        image = Image.open(stream)

        # Resize the image to fit the label
        image = image.resize((640, 480))

        # Convert the image to a Tkinter-compatible format
        photo = ImageTk.PhotoImage(image)

        # Update the label to show the new image
        self.label.config(image=photo)
        self.label.image = photo

        # Schedule the next update
        # self.after(10, self.update_feed, stream)


class CV2Camera:  # Originally a tk object, some stuff may reflect that
    """
    Class for the Camera, place the label in the scene to get the feed on screen
    """

    def __init__(self, root):
        # Set up the camera feed
        self.cap = cv2.VideoCapture(0)

        # set camera resolution to 320x240
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

        # Create a label to display the camera feed
        self.label = tk.Label(root, name="!labelCamera")
        self.label.pack()

        # Continuously update the camera feed on the label
        self.update_label(root)

    def update_label(self, root):
        ret, frame = self.cap.read()
        if ret:
            # convert the OpenCV frame to a PIL image
            img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            # update the Tkinter label with the PIL image
            self.label.imgtk = ImageTk.PhotoImage(img)
            self.label.config(image=self.label.imgtk)
        # schedule the update_label function to be called again in 10 milliseconds
        root.after(10, self.update_label, root)

    def stop_camera(self):
        return self.cap.release()

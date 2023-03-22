import os
import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import io


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

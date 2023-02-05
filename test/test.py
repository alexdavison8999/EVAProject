import tkinter
root = tkinter.Tk()
root.title("Fenster 1")
root.geometry("100x100")
bg = tkinter.PhotoImage(file="assets/view.png")
evaFace = tkinter.PhotoImage(file="evaFace4Home.png")

my_canvas = tkinter.Canvas(root, width=1280, height=800)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")
root.mainloop()
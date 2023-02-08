from pprint import pprint
import tkinter
import os, sys

path = os.path.dirname(__file__)

# new_path = os.path.join(os.path.abspath(os.getcwd()), 'test/')

print(os.path.abspath(os.getcwd()))

# os.path.join(os.path.dirname(__file__),'~/projects/EVAProject/EXPOFILES/')
# sys.path.append(new_path)
# print(os.path.join(os.path.dirname(__file__),'/assets'))
# print(os.path.dirname(__file__))
# print(os.path.abspath(os.getcwd()))

pprint(sys.path)

file_name = os.path.join(path,'assets')

root = tkinter.Tk()
root.title("Fenster 1")
root.geometry("500x500")
bg = tkinter.PhotoImage(name="View",file=f'{file_name}/view.png')
bg = tkinter.PhotoImage(name="View2",file='test/assets/view.png')
# bg = tkinter.PhotoImage(name="View3",file='assets/view.png')
evaFace = tkinter.PhotoImage(file="test/assets/evaFace4Home.png")
# bg = tkinter.PhotoImage(file="~/projects/EVAProject/EXPOFILES/assets/view.png")
# evaFace = tkinter.PhotoImage(file="~/projects/EVAProject/EXPOFILES/assets/evaFace4Home.png")

my_canvas = tkinter.Canvas(root, width=1280, height=800)
my_canvas.pack(fill="both", expand=True)

my_canvas.create_image(0, 0, image=bg, anchor="nw")
root.mainloop()
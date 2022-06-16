from tkinter import *
from tkinter import filedialog
from tkinter import font as tkFont
from tkinter import ttk
import tkinter as tk
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

class MainApplication(tk.Tk):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.title("Metabolite identifier")
        self.master.geometry("200x200")
        self.Buttonfont = tkFont.Font(family="arial", size=15, weight=tkFont.BOLD)

        self.container = tk.Frame(self)
        self.container.grid(row=0, column=0)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        self.frames["convert"] = convert(master=self.container, controller=self)

        self.top_frame = Frame(master)
        self.openFile = convert(self.top_frame, controller=self)

class convert(tk.Frame):
    def __init__(self, master, controller):
        tk.Frame.__init__(self, master)
        self.master = master
        self.controller = controller
        self.Buttonfont = tkFont.Font(family="arial", size=15, weight=tkFont.BOLD)
        self.frame = Frame(master).grid(column=0, row=0)

        self.openfilebutton = Button(self.frame, text="Open File", font=self.Buttonfont, command=self.convert)
        self.openfilebutton.grid(row=0, column=0)

    def convert(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("ascii", "*.ascii"),))
        self.output_filename = self.filename[:-6] + ".txt"

        f = open(self.filename, "r")
        for i in f:
            new_i = i.split(" ")
        f.close()

        f = open(self.output_filename, "w")
        for i in new_i:
            also_i = i.split(",")
            try:
                string = also_i[1] + "\t" + also_i[0] + "\n"
                f.write(string)
            except:
                pass
        f.close()
        print(f"{self.output_filename} written")

if __name__ == "__main__":
    root = Tk()
    main_app = MainApplication(root)
    root.iconbitmap()
    root.mainloop()
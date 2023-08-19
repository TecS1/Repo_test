from tkinter import *
import customtkinter as CTk  

# create root window
root = Tk()
varPrueba = IntVar()
otravar=IntVar()
radiob = CTk.CTkRadioButton(root, variable=otravar, value=1)
radiob.grid(column=2, row=5)

radiob2 = CTk.CTkRadioButton(root, variable=otravar, value=2)
radiob2.grid(column=2, row=6)

radiob3 = CTk.CTkRadioButton(root, variable=otravar, value=3)
radiob3.grid(column=2, row=7)

root.mainloop()
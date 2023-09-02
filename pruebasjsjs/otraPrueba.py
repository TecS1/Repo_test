import tkinter as tk
import customtkinter as ctk

class CheckboxGroup:
    def __init__(self, master, text):
        self.var = tk.IntVar()
        self.checkbox = ctk.CTkCheckBox(master, text=text, variable=self.var, command=self.update_checkboxes)
        self.checkbox.pack()

    def update_checkboxes(self):
        for checkbox_group in checkbox_groups:
            if checkbox_group is not self:
                checkbox_group.var.set(0)

root = tk.Tk()
root.title("Checkbox Example")

checkbox_groups = [
    CheckboxGroup(root, "Checkbox 1"),
    CheckboxGroup(root, "Checkbox 2"),
    CheckboxGroup(root, "Checkbox 3")
]

root.mainloop()

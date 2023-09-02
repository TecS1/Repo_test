import tkinter as tk
import customtkinter as CTk

class CheckboxGroup:
    def __init__(self, master, text, checkbox_groups):
        self.var = tk.IntVar()
        self.checkbox = CTk.CTkCheckBox(master, text=text, variable=self.var, command=self.update_checkboxes)
        self.checkbox.pack()
        self.checkbox_groups = checkbox_groups

    def update_checkboxes(self):
        for checkbox_group in self.checkbox_groups:
            if checkbox_group is not self:
                checkbox_group.var.set(0)
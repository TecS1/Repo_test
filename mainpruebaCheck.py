import tkinter as tk
from PruebaCheck import CheckboxGroup

root = tk.Tk()
root.title("Checkbox Example")

checkbox_groups = []  # Definimos la lista antes de crear las instancias

checkbox_groups.append(CheckboxGroup(root, "Checkbox 1", checkbox_groups))
checkbox_groups.append(CheckboxGroup(root, "Checkbox 2", checkbox_groups))
checkbox_groups.append(CheckboxGroup(root, "Checkbox 3", checkbox_groups))

root.mainloop()
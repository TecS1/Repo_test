import tkinter as tk
import customtkinter as CTk

class RadioButtonGroup:
    def __init__(self, root, label, value, var, jside):
        self.root = root
        self.var = var
        self.value = value
        self.jside = jside

        self.radio_button = CTk.CTkRadioButton(root, text=label, variable=self.var, value=value, text_color='black')
        self.radio_button.pack(side=self.jside)

class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Radio Buttons Example")
        self.root.geometry("800x800")

        '''self.print_button = tk.Button(root, text="Imprimir selección", command=self.print_selection)
        self.print_button.pack()'''
        self.FFFF = CTk.CTkFrame(self.root, fg_color='gray')
        self.FFFF.pack(fill='both', expand=True)

        self.bbb = CTk.CTkLabel(self.FFFF, text='xDxD', fg_color='green', width=1)
        self.bbb.pack(side='left', expand=True)

        self.bbb1 = CTk.CTkLabel(self.FFFF, text='xDxD2', fg_color='red', width=200)
        self.bbb1.pack(side='right', fill='both', expand=True)

    def print_selection(self):

        self.shared_var = CTk.IntVar()  # Crear una variable compartida

        self.group1 = RadioButtonGroup(root, "Opción 1", 1, self.shared_var, 'left')
        self.group2 = RadioButtonGroup(root, "Opción 2", 2, self.shared_var, 'right')
        self.group3 = RadioButtonGroup(root, "Opción 3", 3, self.shared_var, 'bottom')
        self.group4 = RadioButtonGroup(root, "Opción 4", 4, self.shared_var, 'right')

if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
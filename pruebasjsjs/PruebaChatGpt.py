import tkinter as tk
import customtkinter as CTk
from otraPrueba import useState

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("State Example")

        self.texto = useState('hola')

        self.un_label = CTk.CTkLabel(root, text=self.texto.get_value(), text_color='black')
        self.un_label.pack()

        # Use a lambda function to pass arguments to the set_value function
        un_boton = CTk.CTkButton(root, text='cambio', text_color='black', command=lambda: self.update_text('cambio la variable'))
        un_boton.pack()

    def update_text(self, message):
        self.texto.set_value(message)
        self.un_label.configure(text=self.texto.get_value())

root = tk.Tk()
app = App(root)
root.mainloop()

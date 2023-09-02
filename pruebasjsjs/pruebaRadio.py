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

def py_useState(initial_value: any, variable):
    variable = initial_value
    def funcion_de_cambio(cambio):
        nonlocal variable
        variable = cambio

    return variable, funcion_de_cambio

class useState_py():
    def __init__(self, value):
        self.variable = value
    
        def funcion_de_cambio(cambio):
            self.variable = cambio
        return self.variable, funcion_de_cambio
    
class StateManager:
    def __init__(self, initial_value):
        self.variable = StringVar()
        self.variable = initial_value

    def get_value(self):
        return self.variable

    def set_value(self, new_value):
        self.variable = new_value

def py_useState(initial_value: any):
    state_manager = StateManager(initial_value)

    def funcion_de_cambio(cambio):
        state_manager.set_value(cambio)

    return state_manager.get_value(), funcion_de_cambio

class useState():
    def __init__(self, initial_value):
        self.variable = initial_value
    
    def get_value(self):
        return self.variable

    def set_value(self, new_value: str = None):
        if new_value is not None:
            self.variable = new_value
        un_label.configure(text=texto.get_value())

texto = useState('hola')

un_label = CTk.CTkLabel(root, text=texto.get_value, text_color='black')
un_label.grid(column=1, row=8)

un_boton = CTk.CTkButton(root, text='cambio', text_color='black', command=lambda: texto.set_value('cambio la variable'))
un_boton.grid(column=1, row=9)

print(texto)  # Imprime: hola


print(texto)  # Imprime: nuevo texto

root.mainloop()
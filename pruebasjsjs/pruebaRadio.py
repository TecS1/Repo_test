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

def py_useState(var: any, texto):
    la_var = var
    def funcio_de_cambio(cambio):
        nonlocal la_var
        #print(la_var)
        la_var = cambio
        #print(la_var)

    return la_var, funcio_de_cambio


texto, setTexto = py_useState('hola')

un_label = CTk.CTkLabel(root, text=texto, text_color='black')
un_label.grid(column=1, row=8)

un_boton = CTk.CTkButton(root, text='cambio', text_color='black', command=lambda: hola('cambio'))
un_boton.grid(column=1, row=9)

def hola(mensaje):
    setTexto(mensaje)
    un_label.configure(text = texto)
    print(texto)

root.mainloop()
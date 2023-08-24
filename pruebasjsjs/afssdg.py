from tkinter import *
import customtkinter as CTk
 
 
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])
 
# take the data
lst = [(1,'Raj'),
       (2,'Aaryan'),
       (3,'Vaishnavi'),
       (4,'Rachna'),
       (5,'Shubham')]

var = 'xD'
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
# create root window
root = Tk()
t = Table(root)
varPrueba = IntVar()
otravar=IntVar()
otraotravar = StringVar()
otraotravar.set(var)
radiob = CTk.CTkRadioButton(root, variable=otravar, value=1)
radiob.grid(column=2, row=5)

radiob2 = CTk.CTkRadioButton(root, variable=otravar, value=2)
radiob2.grid(column=2, row=6)

radiob3 = CTk.CTkRadioButton(root, variable=otravar, value=3)
radiob3.grid(column=2, row=7)

el_entry = CTk.CTkEntry(root, textvariable=otraotravar, text_color='black')
el_entry.grid(column=2, row=8)

root.mainloop()
import customtkinter

class MyFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.configure(fg_color='blue')
        # add widgets onto the frame, for example:
        self.label = customtkinter.CTkLabel(self, fg_color='green')
        self.label.grid(row=0, column=0, padx=20)

class xDDDD(customtkinter.CTkFrame):
    def __init__(self, *args, Item, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(fg_color='red')


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.grid_rowconfigure(0, weight=1)  # configure grid system
        self.grid_columnconfigure(0, weight=1)

        self.my_frame = MyFrame(self)
        self.my_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


app = App()
app.mainloop()
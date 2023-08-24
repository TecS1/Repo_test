

def py_useState(var: any):
    la_var = var
    def funcio_de_cambio(cambio):
        la_var = cambio
        return la_var

    return la_var, funcio_de_cambio()
        

        

     
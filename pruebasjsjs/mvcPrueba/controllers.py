from views import VistaUsuario
from models import Usuario

class ControladorUsuario:
    def __init__(self):
        self.vista = VistaUsuario()

    def crear_usuario(self, nombre, edad):
        usuario = Usuario(nombre, edad)
        self.vista.mostrar_datos_usuario(usuario)
    
#if __name__ == "__main__":
controlador = ControladorUsuario()
controlador.crear_usuario("Juan", 30)

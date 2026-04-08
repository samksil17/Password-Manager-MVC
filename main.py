from modelo import GestorModel
from vista import GestorVista
from controlador import GestorControlador

if __name__ == "__main__":
    # Instanciamos las tres partes
    mi_modelo = GestorModel()
    mi_vista = GestorVista()
    
    # El controlador coordina a los otros dos
    mi_controlador = GestorControlador(mi_modelo, mi_vista)

    # Arrancamos la aplicación
    mi_vista.mainloop()
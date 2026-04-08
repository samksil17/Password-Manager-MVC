class GestorControlador:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista

        # Aqui le decimos al boton de la vista que funcion ejecutar
        self.vista.btn_guardar.configure(command=self.ejecutar_guardado)

    def ejecutar_guardado(self):
        # 1- Le pedimos los datos a la vista
        datos = self.vista.obtener_datos()

        # Validación simple
        if datos["sitio"] == "" or datos["password"] == "":
            print("Error: El sitio y la contraseña son obligatorios")
            return

        # 2- Le decimos al modelo que los guardes (se encarga de cifrar)
        self.modelo.agregar_contrasena(
            datos["sitio"], 
            datos["usuario"], 
            datos["password"], 
            datos["categoria"]
        )

        # 3- Le decimos a la vista que limpie los cuadros de texto
        self.vista.limpiar_campos()
        print("¡Guardado con éxito y cifrado en el JSON!")
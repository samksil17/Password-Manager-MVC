import customtkinter as ctk

# Configuramos la apariencia general
ctk.set_appearance_mode("dark") 
ctk.set_default_color_theme("blue")

class GestorVista(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.title("Mis Contraseñas Seguras")
        self.geometry("400x450")

        #Creación de los elementos (Widgets)
        self.label_titulo = ctk.CTkLabel(self, text="GESTÓR DE ACCESO", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20)

        self.entry_sitio = ctk.CTkEntry(self, placeholder_text="Nombre del Sitio (ej: Gmail)")
        self.entry_sitio.pack(pady=10, padx=20, fill="x")

        self.entry_usuario = ctk.CTkEntry(self, placeholder_text="Usuario o Correo")
        self.entry_usuario.pack(pady=10, padx=20, fill="x")

        self.entry_pass = ctk.CTkEntry(self, placeholder_text="Contraseña", show="*")
        self.entry_pass.pack(pady=10, padx=20, fill="x")

        self.entry_cat = ctk.CTkEntry(self, placeholder_text="Categoría (ej: Trabajo)")
        self.entry_cat.pack(pady=10, padx=20, fill="x")

        self.btn_guardar = ctk.CTkButton(self, text="Guardar Credencial", fg_color="green")
        self.btn_guardar.pack(pady=20)

    # Función para obtener lo que el usuario escribió
    def obtener_datos(self):
        return {
            "sitio": self.entry_sitio.get(),
            "usuario": self.entry_usuario.get(),
            "password": self.entry_pass.get(),
            "categoria": self.entry_cat.get()
        }

    # Función para limpiar los campos después de guardar
    def limpiar_campos(self):
        self.entry_sitio.delete(0, 'end')
        self.entry_usuario.delete(0, 'end')
        self.entry_pass.delete(0, 'end')
        self.entry_cat.delete(0, 'end')

       
import json
import os
from cryptography.fernet import Fernet


class GestorModel:
    def __init__(self):
        self.archivo_json = "datos.json"
        self.archivo_llave = "secreto.key"
        self.llave = self.cargar_o_crear_llave()
        self.cipher = Fernet(self.llave)

    def cargar_o_crear_llave(self):
        # Si no existe la llave, la creamos y la guardamos en un archivo. Si ya existe, la leemos
        if not os.path.exists(self.archivo_llave):
            nueva_llave = Fernet.generate_key()
            with open(self.archivo_llave, "wb") as f:
                f.write(nueva_llave)
            return nueva_llave
        else:
            with open(self.archivo_llave, "rb") as f:
                return f.read()

    def guardar_datos(self, lista_datos):
        # Convierte la lista de Python a un archivo de texto (JSON)
        with open(self.archivo_json, "w") as f:
            json.dump(lista_datos, f, indent=4)

    def cargar_datos(self):
        # Lee el archivo JSON. Si no existe, devuelve una lista vacia
        if not os.path.exists(self.archivo_json):
            return []
        with open(self.archivo_json, "r") as f:
            return json.load(f)

    def agregar_contrasena(self, sitio, usuario, password, categoria):
        datos = self.cargar_datos()

        # PROCESO DE CIFRADO:
        # 1. Convertimos el texto a "bytes" (.encode())
        # 2. Lo encriptamos con la llave (.encrypt())
        # 3. Lo volvemos a convertir a texto para guardarlo en el JSON (.decode())
        pass_cifrada = self.cipher.encrypt(password.encode()).decode()

        nuevo_item = {
            "sitio": sitio,
            "usuario": usuario,
            "password": pass_cifrada,
            "categoria": categoria
        }

        datos.append(nuevo_item)
        self.guardar_datos(datos)

    def obtener_todo_descifrado(self):
        datos = self.cargar_datos()
        for item in datos:
            # PROCESO DE DESCIFRADO:
            # Hacemos lo contrario para poder mostrar la clave real en la app
            pass_real = self.cipher.decrypt(item["password"].encode()).decode()
            item["password"] = pass_real
        return datos

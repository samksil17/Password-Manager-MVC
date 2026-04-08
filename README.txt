Proyecto para la asignatura: Desarrollo de Aplicaciones con Acceso a Datos

Este software es un gestor de contraseñas de escritorio desarrollado en Python. Permite almacenar credenciales de forma organizada y segura, aplicando principios de Programación Orientada a Objetos (POO) y el patrón de diseño MVC.

## Características de Seguridad (Cifrado)
El requisito principal del proyecto es que las contraseñas no sean visibles en el archivo de persistencia. Para lograr esto:
**Algoritmo**: Se utiliza **Fernet (AES-128 en modo CBC)** a través de la librería "cryptography".
**Proceso:** El sistema genera una clave única ("secreto.key"). Antes de guardar cualquier dato en el JSON, el texto plano se convierte en un *token* cifrado de bytes.
**Persistencia:** Los datos se almacenan en un archivo "datos.json". Si un tercero abre este archivo, solo verá cadenas de caracteres aleatorias en el campo de contraseña.

##Librerías Utilizadas
customtkinter: Interfaz gráfica moderna con soporte para modo oscuro y widgets personalizados.
cryptograph: Implementación de las capas de seguridad y cifrado de los datos sensibles.
json: Manejo de la persistencia de datos en formato de texto estructurado.
os: Gestión de rutas de archivos y verificación de existencia de la clave de seguridad
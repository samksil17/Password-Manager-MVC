#Password Manager MVC

Gestor de contraseñas de escritorio desarrollado en python, aplicando el patrón de diseño MVC (Model-View-Controller) y principios de Programación Orientada a Objetos (POO).

Proyecto desarrollado para la asignatura: Desarrollo de Aplicaciones con Acceso a Datos — Institución Universitaria Americana.



## Descripción

Password Manager MVC permite almacenar, consultar y eliminar credenciales (sitio, usuario y contraseña) de forma organizada y segura. Las contraseñas se cifran antes de guardarse, por lo que nunca se almacenan en texto plano.



## Estructura del Proyecto

Password-Manager-MVC/
│
├── main.py           # Punto de entrada de la aplicación
├── modelo.py         # Capa de datos: lógica de negocio y persistencia
├── vista.py          # Capa de presentación: interfaz gráfica (CustomTkinter)
├── controlador.py    # Capa de control: coordina Modelo y Vista
├── datos.json        # Archivo de persistencia (contraseñas cifradas)
├── secreto.key       # Clave de cifrado generada automáticamente
└── README.md


## Patrón MVC — Diseño de la Aplicación

El proyecto está organizado en tres capas bien definidas, siguiendo el patrón Model-View-Controller:

###  Modelo (`modelo.py`)
- Define la lógica de negocio y el acceso a datos.
- Maneja la lectura y escritura en `datos.json`.
- Implementa el cifrado y descifrado de contraseñas usando el algoritmo Fernet (AES-128 CBC)
- Genera y gestiona la clave de cifrado (`secreto.key`).
- No conoce la interfaz gráfica ni el controlador.**

### Vista (`vista.py`)
- Construida con CustomTkinter para una interfaz moderna con soporte para modo oscuro.
- Muestra los formularios de entrada (sitio, usuario, contraseña).
- Presenta la lista de credenciales almacenadas.
- No contiene lógica de negocio: solo presenta información y captura acciones del usuario.

### Controlador (`controlador.py`)
- Actúa como intermediario entre el Modelo y la Vista.
- Recibe los eventos de la Vista (clics de botones).
- Llama al Modelo para guardar, listar o eliminar credenciales.
- Devuelve los resultados a la Vista para mostrarlos.
- Mantiene los controladores delgados: sin lógica de negocio ni SQL directo.

### Main (`main.py`)
- Punto de entrada único de la aplicación.
- Crea la instancia del Controlador, que a su vez inicializa el Modelo y la Vista.
- Lanza el bucle principal de la interfaz gráfica (`mainloop()`).


## Seguridad y Cifrado

| Aspecto | Detalle |
|---|---|
| Algoritmo | Fernet (AES-128 en modo CBC con HMAC-SHA256) |
| Librería | `cryptography` |
| Clave | Generada automáticamente en `secreto.key` (una sola vez) |
| Persistencia | `datos.json` — las contraseñas se guardan como tokens cifrados |
| Resultado | Si alguien abre `datos.json`, solo verá cadenas de bytes aleatorios |


## Tecnologías Utilizadas

| Librería | Uso |
|---|---|
| `customtkinter` | Interfaz gráfica moderna (modo oscuro, widgets personalizados) |
| `cryptography` | Cifrado Fernet de contraseñas |
| `json` | Persistencia de datos estructurados |
| `os` | Gestión de rutas y verificación de archivos |

---

## Instalación y Ejecución

### 1. Clona el repositorio con bash
git clone https://github.com/samksil17/Password-Manager-MVC.git
cd Password-Manager-MVC


### 2. Instala las dependencias
pip install customtkinter cryptography

### 3. Ejecuta la aplicación
python main.py


> La primera vez se generará automáticamente el archivo `secreto.key`. No lo elimines o perderás acceso a las contraseñas guardadas.


## Funcionalidades

- Agregar credenciales (sitio, usuario, contraseña)
- Listar todas las credenciales almacenadas
- Eliminar credenciales
- Contraseñas cifradas con Fernet
- Interfaz gráfica moderna con CustomTkinter
- Persistencia en archivo JSON local

## Autor

Samir Kalil 
Institución Universitaria Americana — 2026

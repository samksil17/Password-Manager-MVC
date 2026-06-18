# Password Manager — Evolución Full-Stack

Proyecto desarrollado para la asignatura **Desarrollo de Aplicaciones con Acceso a Datos**  
Institución Universitaria Americana · 2026 · Autor: Samir Kalil

---

## Evolución del proyecto a lo largo del semestre

| Parcial | Stack | Persistencia | Interfaz |
|---------|-------|--------------|---------|
| Parcial 1 | Python + MVC | Archivos JSON (cifrado Fernet) | CustomTkinter (escritorio) |
| Parcial 2 | Python + MVC | Base de datos relacional (MySQL) | CustomTkinter (escritorio) |
| **Parcial 3** | **Flask + SQLAlchemy** | **PostgreSQL (Render)** | **Web — HTML + Bootstrap (GitHub Pages)** |

---

## Estructura del repositorio

```
Password-Manager-MVC/
├── main.py           → Punto de entrada (Parcial 1)
├── modelo.py         → Capa Modelo: JSON + cifrado Fernet (Parcial 1)
├── vista.py          → Capa Vista: GUI con CustomTkinter (Parcial 1)
├── controlador.py    → Capa Controlador (Parcial 1)
├── backend/          → API REST - Parcial 3
│   ├── app.py        → Controlador: rutas Flask + endpoints CRUD
│   ├── models.py     → Modelo: ORM con SQLAlchemy (tabla Credential)
│   └── requirements.txt
└── docs/             → Frontend - Parcial 3
    └── index.html    → Vista: HTML + Bootstrap + JavaScript (fetch API)
```

---

## Parcial 3 — Aplicación Web Full-Stack

### Arquitectura MVC web

```
[Vista]        docs/index.html      HTML + Bootstrap + JS (GitHub Pages)
   ↓ fetch()
[Controlador]  backend/app.py       Rutas Flask (API REST)
   ↓ ORM
[Modelo]       backend/models.py    SQLAlchemy → PostgreSQL (Render)
```

### Endpoints de la API

| Método | Ruta | Descripción |
|--------|------|-------------|
| GET | `/credentials` | Lista todas las credenciales |
| POST | `/credentials` | Crea una nueva credencial |
| GET | `/credentials/<id>` | Obtiene una credencial por ID |
| PUT | `/credentials/<id>` | Actualiza una credencial |
| DELETE | `/credentials/<id>` | Elimina una credencial |

### Correr el backend localmente

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python app.py
```

API disponible en `http://localhost:5000`

---

## Despliegues

- **Backend (API):** https://password-manager-backend.onrender.com
- **Frontend:** https://samksil17.github.io/Password-Manager-MVC

---

## Parcial 1 — Aplicación de escritorio

```bash
pip install customtkinter cryptography
python main.py
```
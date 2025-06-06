# Calculadora con FastAPI

Este proyecto es una calculadora básica implementada como un microservicio utilizando **FastAPI**. Permite realizar operaciones aritméticas simples a través de una API REST y una interfaz web con HTML y JavaScript.

---

## Características

-  Suma
-  Resta
-  Multiplicación
-  División (con manejo de errores)
-  Interfaz web (HTML + JS)
-  API con FastAPI y Uvicorn

---

## Estructura del proyecto

calculadora/
│
├── static/
│ ├── index.html
│ └── js/
├── main.py
└── README.md


---

##  Instalación y uso

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/nombre-del-repositorio.git
cd nombre-del-repositorio

---

## Instala dependencias:

pip install fastapi uvicorn


Ejecuta la aplicación:

python -m uvicorn main:app --reload

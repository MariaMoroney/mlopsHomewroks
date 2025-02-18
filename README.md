# API de Usuarios - Trabajo Práctico 2

Este proyecto implementa dos APIs simples utilizando FastAPI: una para crear usuarios (POST) y otra para obtenerlos (GET). El proyecto demuestra un flujo de trabajo de control de versiones utilizando Git y GitHub.

## Estructura del proyecto

- `main.py`: Contiene la implementación de los endpoints de la API
- `requirements.txt`: Lista de dependencias necesarias

## Endpoints implementados

### POST /users/
Permite crear un nuevo usuario con los siguientes campos:
- id: int (identificador único)
- name: str (nombre del usuario)
- email: str (correo electrónico)

### GET /users/{user_id}
Obtiene un usuario específico por su ID

### GET /users/
Obtiene la lista de todos los usuarios creados

## Configuración del entorno

1. Clonar el repositorio:
git clone https://github.com/MariaMoroney/mlopsHomewroks.git
cd api-users-tp2

2. Crear y activar entorno virtual:
python3 -m venv venv
source venv/bin/activate  # En Mac/Linux

3. Instalar dependencias:
pip install -r requirements.txt

4. Ejecutar la aplicación:
uvicorn main:app --reload

5. Acceder a la documentación interactiva:
Abre tu navegador en `http://127.0.0.1:8000/docs`

## Flujo de trabajo Git

Este proyecto sigue un flujo de trabajo de Git con las siguientes ramas:
- `main`: Rama principal (producción)
- `staging`: Rama de pre-producción
- `develop`: Rama de desarrollo
- Ramas de características: `feature-post-user`, `feature-get-user`

## Autor

[Maria Fernanda Moroney Sole]


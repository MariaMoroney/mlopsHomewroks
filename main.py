from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="API Users TP2")


# Modelo de datos para el usuario
class User(BaseModel):
    id: int
    name: str
    email: str


# Lista para almacenar usuarios
users = []


@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Usuarios"}


@app.post("/users/", response_model=User)
def create_user(user: User):
    # Verificar si ya existe un usuario con el mismo ID
    for existing_user in users:
        if existing_user.id == user.id:
            raise HTTPException(status_code=400, detail="El ID de usuario ya existe")

    # Agregar el nuevo usuario a la lista
    users.append(user)
    return user
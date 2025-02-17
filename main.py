from fastapi import FastAPI

app = FastAPI(title="API Users TP2")

# Lista para almacenar usuarios
users = []

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Usuarios"}
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# Servir archivos estáticos (HTML)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def root():
    return FileResponse("static/index.html")

@app.get("/suma")
def sumar(a: float, b: float):
    return {"operacion": "suma", "resultado": a + b}

@app.get("/resta")
def restar(a: float, b: float):
    return {"operacion": "resta", "resultado": a - b}

@app.get("/multiplica")
def multiplicar(a: float, b: float):
    return {"operacion": "multiplicacion", "resultado": a * b}

@app.get("/divide")
def dividir(a: float, b: float):
    if b == 0:
        raise HTTPException(status_code=400, detail="No se puede dividir entre cero")
    return {"operacion": "division", "resultado": a / b}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Gosta de Bee Gees? Minha música preferida se chama Too Much Heaven"}


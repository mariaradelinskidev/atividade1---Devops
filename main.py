from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Olá professor, adorei a matéria"}


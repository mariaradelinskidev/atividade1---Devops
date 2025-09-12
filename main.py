from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Island in the stream também é muito boa"
            "Baby, when I met you, there was peace unknown "
            "I set out to get you with a fine-tooth comb"
            "I was soft inside"
            "There was something going on"}
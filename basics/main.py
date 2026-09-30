from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {'message': "HI"}

@app.get("/hello")
def hello():
    return {'message': "Hello"}
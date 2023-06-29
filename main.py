from fastapi import FastAPI
from pydantic import BaseModel

app: FastAPI = FastAPI()

class Decimales(BaseModel):
      decimal= int

@app.get("/")
def read_root():
    return{"Hello": "Mundo"}

@app.get("/decimal")
def Decim():
    #decimal = [:2]
    return{"Hello": "decimal"}
from fastapi import FastAPI 
from typing import Optional # module typing class Optional
from pydantic import BaseModel
app = FastAPI()

class User(BaseModel):
    username : str
    password : str
    level : Optional[str] = "normal"

@app.get("/")
async def root():
    return {"message": "Hello Jewy"}

@app.get("/hi")
def hi(name:str,reply: str):
    return {"Hi":name, "reply":reply}

@app.get("/items/{item_id}")
def read(item_id:int,name:str,reply: Optional[str] = None):
    return {"ID":item_id,"Item":name, "reply":reply}

@app.post("/login")
def login(user: User):
    return {"echo":user}

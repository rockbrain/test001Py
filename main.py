from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str = None
    price: float

@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

from fastapi import FastAPI, HTTPException
from typing import List
from .models import Item
from .crud import get_items, get_item, create_item, update_item, delete_item
from .schemas import ItemCreate, ItemUpdate

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API déployée avec succès sur Render !"}

@app.get("/items", response_model=List[Item])
def read_items():
    return get_items()

@app.get("/items/{id}", response_model=Item)
def read_item(id: int):
    db_item = get_item(id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.post("/items", response_model=Item)
def create_item_view(item: ItemCreate):
    return create_item(item)

@app.put("/items/{id}", response_model=Item)
def update_item_view(id: int, item: ItemUpdate):
    db_item = update_item(id, item)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{id}")
def delete_item_view(id: int):
    result = delete_item(id)
    if not result:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"message": "Item deleted successfully"}

from .models import Item
from .schemas import ItemCreate, ItemUpdate

# Base de données fictive
items = []

def get_items():
    return items

def get_item(item_id: int):
    return next((item for item in items if item.id == item_id), None)

def create_item(item: ItemCreate):
    new_item = Item(id=len(items) + 1, **item.dict())
    items.append(new_item)
    return new_item

def update_item(item_id: int, item: ItemUpdate):
    db_item = get_item(item_id)
    if db_item:
        db_item.name = item.name
        db_item.price = item.price
        db_item.in_stock = item.in_stock
        return db_item
    return None

def delete_item(item_id: int):
    global items
    item_to_delete = get_item(item_id)
    if item_to_delete:
        items = [item for item in items if item.id != item_id]
        return True
    return False

from pydantic import BaseModel

# Schéma pour la création d'un item
class ItemCreate(BaseModel):
    name: str
    price: float
    in_stock: bool

# Schéma pour la mise à jour d'un item
class ItemUpdate(BaseModel):
    name: str
    price: float
    in_stock: bool

from app.crud import create_item, get_item
from app.schemas import ItemCreate

def test_create_and_get_item():
    item = ItemCreate(name="Livre", price=12.0, in_stock=True)
    created = create_item(item)
    fetched = get_item(created.id)
    assert fetched.name == "Livre"
    assert fetched.price == 12.0

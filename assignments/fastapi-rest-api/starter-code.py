from typing import List, Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class ItemRequest(BaseModel):
    name: str
    category: str
    price: float
    in_stock: bool

class ItemResponse(ItemRequest):
    item_id: int

# Sample data store
items = [
    {"item_id": 1, "name": "Python Book", "category": "books", "price": 29.99, "in_stock": True},
    {"item_id": 2, "name": "Wireless Mouse", "category": "electronics", "price": 19.99, "in_stock": False},
]

@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int):
    for item in items:
        if item["item_id"] == item_id:
            return item
    return {"item_id": item_id, "name": "Unknown", "category": "unknown", "price": 0.0, "in_stock": False}

@app.get("/items", response_model=List[ItemResponse])
def list_items(category: Optional[str] = None, max_price: Optional[float] = None):
    filtered_items = items
    if category:
        filtered_items = [item for item in filtered_items if item["category"] == category]
    if max_price is not None:
        filtered_items = [item for item in filtered_items if item["price"] <= max_price]
    return filtered_items

@app.post("/items", response_model=ItemResponse)
def create_item(item: ItemRequest):
    new_item_id = max(item["item_id"] for item in items) + 1 if items else 1
    new_item = {"item_id": new_item_id, **item.dict()}
    items.append(new_item)
    return new_item

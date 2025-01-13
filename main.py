from typing import Optional

import uvicorn
from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel

# Initialize FastAPI app
app = FastAPI()

# --- Pydantic Models for Request/Response ---
class Item(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    
class User(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None

# --- Basic Routes ---
@app.get("/")
async def root():
    """Basic GET endpoint returning a welcome message"""
    return {"message": "Welcome to FastAPI! ECE140"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    """Path parameter example"""
    return {"message": f"Hello, {name}!"}

# --- Query Parameters --- 
# Example /items/?skip=0&limit=10
@app.get("/items/")
async def read_items(
    start: int = Query(default=0, description="Number of items to start at"),
    limit: int = Query(default=10, ge=1, le=100, description="Number of items to return")
):
    """Query parameters example with validation"""
    fake_items = [{"item_id": i} for i in range(start, start + limit)]
    return fake_items

# --- Request Body ---
# Example /items/
@app.post("/items/")
async def create_item(item: Item):
    """POST endpoint with request body validation using Pydantic"""
    return {"item": item, "message": "Item created successfully"}

# --- Path Parameters with Validation ---
# Example /items/42?q=test
@app.get("/items/{item_id}")
async def read_item(
    item_id: int = Path(..., ge=1, description="The ID of the item to retrieve"),
    q: Optional[str] = Query(None, max_length=50)
):
    """Path parameter with validation and optional query parameter"""
    if item_id == 42:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"item_id": item_id, "q": q}

# Run the server
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

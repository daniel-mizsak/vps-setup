"""
Simple FastAPI application.

@author "Daniel Mizsak" <info@pythonvilag.hu>
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "My Motivated World!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

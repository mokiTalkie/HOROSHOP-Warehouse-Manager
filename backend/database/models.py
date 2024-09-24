from pydantic import BaseModel, Field

class User(BaseModel):
    id: int = Field(alias="_id")
    name: str

class Product(BaseModel):
    id: str
    name: str

class Order(BaseModel):
    id: int

class Shelf(BaseModel):
    id: int

class Rack(BaseModel):
    id: int

class Warehouse(BaseModel):
    name: str
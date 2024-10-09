from pydantic import BaseModel, Field, EmailStr, HttpUrl

class Contacts(BaseModel):
    email: EmailStr | None
    phone: str = Field(pattern=r"^\+380\d{9}$")
    url: HttpUrl | None

class User(BaseModel):
    id: int = Field(alias="_id")
    email: str
    name: str = None
    photo: str = None

    class Config:
        populate_by_name = True

class Supplier(BaseModel):
    id: int = Field(alias="_id")
    name: str

class Category(BaseModel):
    id: int = Field(alias="_id")
    parent_id: int
    name: str
    specs_range: str

class Product(BaseModel):
    id: str
    category_id: int
    article: str
    name: str

# class Order(BaseModel):
#     id: int

# class Shelf(BaseModel):
#     id: int

# class Rack(BaseModel):
#     id: int

# class Warehouse(BaseModel):
#     name: str
from pydantic import BaseModel, Field, EmailStr, HttpUrl

class Contacts(BaseModel):
    email: EmailStr | None
    phone: str = Field(pattern=r"^\+380\d{9}$")
    url: HttpUrl | None

class User(BaseModel):
    id: int = Field(alias="_id")
    email: EmailStr
    name: str

class Supplier(BaseModel):
    id: int = Field(alias="_id")
    name: str

class Category(BaseModel):
    id: int = Field(alias="_id")
    parent_id: int
    name: str

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
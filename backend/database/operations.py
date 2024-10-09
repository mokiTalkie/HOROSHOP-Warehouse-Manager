from .config import DB_CLIENT
from .models import Product, User


def add_product(product: Product, is_new: bool, rack_id: int, shelf_id: int) -> bool:
    pass


def replace_product(
    product: Product,
    from_rack_id: int,
    from_shelf_id: int,
    to_rack_id: int,
    to_shelf_id: int,
) -> bool:
    pass


def reserve_product(products: dict[str | int]) -> bool:
    pass


def delete_product(product: Product) -> bool:
    pass


def add_shelf(rack_id: int) -> bool:
    pass


def delete_shelf(shelf_id: int, rack_id: int) -> bool:
    pass


def add_rack() -> bool:
    pass


def delete_rack(rack_id: int) -> bool:
    pass


async def get_user(email: str) -> User | None:
    user = DB_CLIENT["Users"].find_one(filter={"email": email})
    if user:
        return User(**user)
    else:
        return None


def update_user(user: User) -> bool:
        DB_CLIENT["Users"].find_one_and_update(filter={"_id": user.id}, update={"$set": user.model_dump(by_alias=True)}, upsert=True)
        return True

#TODO
def delete_user(id: str) -> bool:
    pass

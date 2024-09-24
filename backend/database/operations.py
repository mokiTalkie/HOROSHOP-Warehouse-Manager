from .config import DB_CLIENT
from .models import Product


def add_product(product: Product, is_new: bool, rack_id: int, shelf_id: int) -> bool:
    pass

def replace_product(product: Product, from_rack_id: int, from_shelf_id: int, to_rack_id: int, to_shelf_id: int) -> bool:
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


from pydantic import BaseModel

class Product(BaseModel):
    id : int
    name : str
    price: float
    in_stock: bool = True


product1 = Product(id=101, name="laptop", price=5555.7, in_stock= False)
product2 = Product(id=102, name="mobile", price=55.7)
product3 = Product(name="laptop")
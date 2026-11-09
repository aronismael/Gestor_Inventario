from pydantic import BaseModel

class producto(BaseModel):

    NombreProducto: str
    Sku: str
    Category: str
    stock: int
    Price: float
    Status: float
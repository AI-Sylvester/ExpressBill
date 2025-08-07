from pydantic import BaseModel

class OrderRequest(BaseModel):
    barcode: str
    quantity: int
    discount: float

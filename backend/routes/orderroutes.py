from fastapi import APIRouter
from db import get_db1_connection
from models import OrderRequest

router = APIRouter()

@router.post("/order")
def create_order(order: OrderRequest):
    conn = get_db1_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO OrderDetails (Barcode, Quantity, Discount) VALUES (?, ?, ?)",
        order.barcode, order.quantity, order.discount
    )
    conn.commit()
    conn.close()
    return {"message": "Order saved"}

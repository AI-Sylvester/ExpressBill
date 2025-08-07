from fastapi import APIRouter, HTTPException
from db import get_db2_connection

router = APIRouter()

@router.get("/item/{barcode}")
def get_item(barcode: str):
    conn = get_db2_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT Barcode, Particulars, ItemCategoryCode1, ItemCategoryCode2, SalesTax1Per, SaleRate FROM StockMas WHERE Barcode = ?", (barcode,))
        row = cursor.fetchone()
    finally:
        conn.close()

    if row:
        return {
            "barcode": row.Barcode,
            "particulars": row.Particulars,
            "category1": row.ItemCategoryCode1,
            "category2": row.ItemCategoryCode2,
            "tax_percent": float(row.SalesTax1Per),
            "rate": float(row.SaleRate)
        }

    raise HTTPException(status_code=404, detail="Item not found")

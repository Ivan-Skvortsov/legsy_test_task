from pydantic import BaseModel


class ProductResponse(BaseModel):
    nm_id: int
    name: str
    brand: str
    brand_id: int
    site_brand_id: int
    supplier_id: int
    sale: int
    price: int
    sale_price: int
    rating: int
    feedbacks: int
    colors: list
    quantity: int

    class Config:
        orm_mode = True

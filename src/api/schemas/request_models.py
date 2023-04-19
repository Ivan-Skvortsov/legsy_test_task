from pydantic import BaseModel, Field


class CreateOrUpdateProductRequest(BaseModel):
    """Requsest schema for creating or updating product."""
    nm_id: int = Field(..., alias="idw")
    name: str
    brand: str
    brand_id: int = Field(..., alias="brandId")
    site_brand_id: int = Field(..., alias="siteBrandId")
    supplier_id: int = Field(..., alias="supplierId")
    sale: int
    price: int = Field(..., alias="priceU")
    sale_price: int = Field(..., alias="salePriceU")
    rating: int
    feedbacks: int
    colors: list
    quantity: int


class ParseProductRequest(BaseModel):

    nm_id: int
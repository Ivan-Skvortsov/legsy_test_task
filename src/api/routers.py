from http import HTTPStatus

from fastapi import APIRouter, Depends

from src.api.schemas.response_models import ProductResponse
from src.api.schemas.request_models import ParseProductRequest
from src.crud.product import ProductCRUD
from src.models.product import Product
from src.services.parsing import get_product_data

product_router = APIRouter(prefix="/products", tags=["Products"])


@product_router.post(
    "/",
    response_model=ProductResponse,
    status_code=HTTPStatus.CREATED,
    summary="Parse wildberries.ru and save to db product with given nm_id.",
    response_description="Product info.",
)
async def parse_wildberries_and_save_product(
    parse_product_data: ParseProductRequest,
    product_crud: ProductCRUD = Depends()
) -> ProductResponse:
    product_data = get_product_data(parse_product_data.nm_id)
    product = Product(**product_data.dict())
    return await product_crud.create(product)


@product_router.get(
    "/",
    response_model=list[ProductResponse],
    status_code=HTTPStatus.OK,
    summary="Get products list.",
    response_description="List of all existing products."
)
async def list_products(
    product_crud: ProductCRUD = Depends()
) -> list[ProductResponse]:
    return await product_crud.list()


@product_router.get(
    "/{nm_id}",
    response_model=ProductResponse,
    status_code=HTTPStatus.OK,
    summary="Get product by nm_id.",
    response_description="Product info."
)
async def get_product_by_nm_id(
    nm_id: int,
    product_crud: ProductCRUD = Depends()
) -> ProductResponse:
    return await product_crud.get_one_or_none(nm_id)


@product_router.delete(
    "/{nm_id}",
    status_code=HTTPStatus.NO_CONTENT,
    summary="Delete product with given nm_id.",
)
async def delete_product_by_nm_id(
    nm_id: int,
    product_crud: ProductCRUD = Depends()
) -> None:
    return await product_crud.delete(nm_id)

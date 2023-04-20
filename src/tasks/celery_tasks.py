from typing import AsyncGenerator
import asyncio

from celery import Celery

from src.configs.database import get_session
from src.crud.product import ProductCRUD
from src.models.product import Product
from src.services.parser import get_product_data
from src.configs.environment import settings


celery_app = Celery("tasks", broker=settings.CELERY_BROKER_URL)


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        60,
        update_all_products_info_task.s(),
        name="update all products info"
    )


@celery_app.task
def update_all_products_info_task():
    asyncio.run(update_all_products_info())


async def get_product_crud_callback(
    session_generator: AsyncGenerator
) -> ProductCRUD:
    session = await anext(session_generator)
    return ProductCRUD(session)


async def update_all_products_info(
    chunk_size: int = 5,
    short_sleep: float = .2,
    long_sleep: float = 1
) -> None:
    """Update all products in database.

    Args:
        chunk_size: request chunk size
        short_sleep: sleep time between each request
        long_sleep: sleep time between each chunk of requests
    """
    session_generator = get_session()
    product_crud = await get_product_crud_callback(session_generator)
    product_ids = await product_crud.get_item_numbers_of_all_products()
    count = 0
    for nm_id in product_ids:
        product_data = get_product_data(nm_id)
        product = Product(**product_data.dict())
        await product_crud.update(nm_id, product)
        await asyncio.sleep(short_sleep)
        count += 1
        if count == chunk_size:
            await asyncio.sleep(long_sleep)
            count = 0

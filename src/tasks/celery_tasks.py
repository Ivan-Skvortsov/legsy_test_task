from contextlib import asynccontextmanager
import asyncio

from celery import Celery
from sqlalchemy.ext.asyncio import async_scoped_session


from src.configs.database import async_session
from src.crud.product import ProductCRUD
from src.models.product import Product
from src.services.parser import get_product_data
from src.configs.environment import settings


celery_app = Celery("tasks", broker=settings.CELERY_BROKER_URL)

loop = asyncio.get_event_loop()


@celery_app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        settings.PRODUCT_UPDATE_PERIOD_SECONDS,
        update_all_products_info_task.s(),
        name="update all products info"
    )


@celery_app.task
def update_all_products_info_task():
    loop.run_until_complete(update_all_products_info())


@asynccontextmanager
async def scoped_session():
    scoped_factory = async_scoped_session(
        async_session,
        scopefunc=update_all_products_info
    )
    try:
        async with scoped_factory() as session:
            yield session
    finally:
        await scoped_factory.remove()


async def update_all_products_info(
    chunk_size: int = 5,
    short_sleep: float = .2,
    long_sleep: float = 1
) -> None:
    """Update all products in database.

    Args:
        chunk_size: requests chunk size
        short_sleep: sleep time between each request
        long_sleep: sleep time between each chunk of requests
    """
    async with scoped_session() as session:
        product_crud = ProductCRUD(session)
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

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.services.parsing import get_product_data
from src.configs.database import get_session
from src.models.product import Product
from src.routers.product import product_router

app = FastAPI()
app.include_router(product_router)


@app.get("/")
async def hello_world(session: AsyncSession = Depends(get_session)):
    product_data = get_product_data(139760729)
    product = Product(**product_data.dict())
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


if __name__ == "__main__":
    uvicorn.run(app)

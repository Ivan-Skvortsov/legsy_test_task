from typing import Optional

from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Product
from src.configs.database import get_session
from src.api.exceptions import ItemNotFoundError, ItemAlreadyExistsError


class ProductCRUD:

    def __init__(self, session: AsyncSession = Depends(get_session)) -> None:
        self.__session = session

    async def get_one_or_none(self, nm_id: int) -> Optional[Product]:
        db_obj = await self.__session.execute(
            select(Product).where(Product.nm_id == nm_id)
        )
        return db_obj.scalars().first()

    async def create(self, instance: Product) -> Product:
        if await self.get_one_or_none(instance.nm_id):
            raise ItemAlreadyExistsError
        self.__session.add(instance)
        await self.__session.commit()
        await self.__session.refresh(instance)
        return instance

    async def list(self) -> list[Product]:
        db_objs = await self.__session.scalars(select(Product))
        return db_objs.all()

    async def update(self, nm_id: int, instance: Product) -> Product:
        instance.nm_id = nm_id
        instance = await self.__session.merge(instance)
        await self.__session.commit()
        return instance

    async def delete(self, nm_id: int) -> None:
        db_obj = await self.get_one_or_none(nm_id)
        if not db_obj:
            raise ItemNotFoundError
        await self.__session.delete(db_obj)
        await self.__session.commit()
        await self.__session.flush()

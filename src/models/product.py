from sqlalchemy import Column, Integer, JSON, String

from src.models.base import Base


class Product(Base):

    nm_id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    brand = Column(String(100), nullable=False)
    brand_id = Column(Integer, nullable=False)
    site_brand_id = Column(Integer, nullable=False)
    supplier_id = Column(Integer, nullable=False)
    sale = Column(Integer, nullable=False)
    price = Column(Integer, nullable=False)
    sale_price = Column(Integer, nullable=False)
    rating = Column(Integer, nullable=False)
    feedbacks = Column(Integer, nullable=False)
    colors = Column(JSON, nullable=False)
    quantity = Column(Integer, nullable=False)

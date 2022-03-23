# coding: utf-8
from sqlalchemy import Column, Index, Integer, String, TIMESTAMP, text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ProductStock(Base):
    __tablename__ = 'product_stocks'
    __table_args__ = (
        Index('uq_category_check_time', 'category', 'check_time', unique=True),
    )

    stock_id = Column(Integer, primary_key=True)
    category = Column(String(100, 'utf8_unicode_ci'), nullable=False, index=True)
    stock = Column(Integer, nullable=False, index=True)
    check_time = Column(TIMESTAMP, nullable=False, index=True, server_default=text("CURRENT_TIMESTAMP"))

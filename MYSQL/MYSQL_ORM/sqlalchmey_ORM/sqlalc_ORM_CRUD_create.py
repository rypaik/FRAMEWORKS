
from db_connection import Session
from product_stocks import ProductStock

product = ProductStock(category="Laptops", stock=999)

with Session() as sess:
    sess.add(product)
    sess.commit()

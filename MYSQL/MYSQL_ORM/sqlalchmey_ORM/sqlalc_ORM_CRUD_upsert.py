
with Session() as sess:
    product_new = ProductStock(stock_id=1, category="Laptops", stock=2000)
    # sess.add(product_new) will raise a Duplicate entry exception.
    sess.merge(product_new)
    sess.commit()

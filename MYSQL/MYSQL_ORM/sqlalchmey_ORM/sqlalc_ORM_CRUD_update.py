
with Session() as sess:
    result = (
        sess.query(ProductStock).filter(ProductStock.stock_id == 1).first()
    )
    result.stock = 1000
    sess.add(result)
    sess.commit()


with Session() as sess:
    result = (
        sess.query(ProductStock).filter(ProductStock.stock_id == 1).first()
    )
    sess.delete(result)
    sess.commit()

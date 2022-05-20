
with Session() as sess:
    result1 = (
        sess.query(ProductStock).filter(ProductStock.stock_id == 1).first()
    )
    result2 = sess.query(ProductStock).filter_by(stock_id=1).first()
    result1 is result2
    # True
    print(result1.stock_id, result1.category, result1.stock)
    # 1 Laptops 999

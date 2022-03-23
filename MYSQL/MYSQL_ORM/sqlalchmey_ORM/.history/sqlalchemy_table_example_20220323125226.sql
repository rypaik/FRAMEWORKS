CREATE DATABASE data;

CREATE TABLE `data`.`product_stocks` (
  `stock_id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(100) NOT NULL,
  `stock` int(11) NOT NULL,
  `check_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`stock_id`),
  UNIQUE KEY `uq_category_check_time` (`category`,`check_time`),
  KEY `ix_category` (`category`),
  KEY `ix_stock` (`stock`),
  KEY `ix_check_time` (`check_time`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci
;

INSERT INTO `data`.`product_stocks`
    (stock_id, category, stock, check_time)
VALUES
    (1, 'Laptops', 999, '2022-01-01 12:12:26'),
    (2, 'Tablets', 888, '2022-01-01 12:12:26'),
    (3, 'Laptops', 777, '2022-01-05 12:12:26'),
    (4, 'Tablets', 666, '2022-01-05 12:12:26'),
    (5, 'Laptops', 555, '2022-01-09 12:12:26'),
    (6, 'Tablets', 444, '2022-01-09 12:12:26')
;
# Learn the basics and get started with SQLAlchemy ORM

> We have introduced how to execute plain SQL queries with SQLAlchemy in Python, which is convenient if you are a SQL master but don’t have…

We have introduced how to execute plain SQL queries with SQLAlchemy in Python, which is convenient if you are a SQL master but don’t have much knowledge about Python or SQLAlchemy yet. However, once you are familiar enough, you would want to write more pythonic code to interact with databases, which can be achieved by the SQLAlchemy **O**bject **R**elational **M**apper (**ORM**).

> [ORM](https://docs.sqlalchemy.org/en/14/orm/tutorial.html) presents a method of associating user-defined Python classes with database tables, and instances of those classes (objects) with rows in their corresponding tables.

![](https://miro.medium.com/max/700/0*wrvas_LBnXOoMK9g.jpg)

Image from [Pixabay](https://pixabay.com/illustrations/server-servers-data-computer-5451985/).

ORM can be overwhelming when it’s first used because there are a lot of new concepts and the special syntax for CRUD operations. In this post, we will introduce the most common concepts and provide easy-to-follow step-by-step instructions for common CRUD operations. You will get a quick start or refresh for ORM after this post.

It’s highly recommended to check [the post for plain SQL queries](https://lynn-kwong.medium.com/how-to-execute-plain-sql-queries-with-sqlalchemy-627a3741fdb1) first because there are detailed introductions for the system setup and the very fundamental concepts such as dialect, driver, Engine, Connection, etc. However, it’s not mandatory. You can just follow the essential steps below to set up the environment for this tutorial. Or you can just read through the code and explanations and will also learn quite a lot, especially when you want to have a quick refresh.

For this tutorial, we need to have a MySQL server running locally. It’s recommended to use Docker to start a MySQL container locally for learning purposes. In this way, you can use any version of MySQL and can avoid potential port conflicts.

Before we use SQLAlchemy to connect to our database and create some ORM models, we need to install the package and its dependencies. It’s recommended to install the packages in a [virtual environment](moz-extension://17b1b930-1e78-454a-b8c8-d7189d1b6084/codex/how-to-create-virtual-environments-with-venv-and-conda-in-python-31814c0a8ec2) so it won’t mess up your system libraries. You can use _venv_ or _conda_ to create a virtual environment in Python. It’s recommended to use [_conda_](moz-extension://17b1b930-1e78-454a-b8c8-d7189d1b6084/codex/how-to-create-virtual-environments-with-venv-and-conda-in-python-31814c0a8ec2) because you can install a specific version of Python in the virtual environment:

Packages installed for this tutorial:

*   [_SQLAlchemy_](https://pypi.org/project/SQLAlchemy/) — The main package that will be used to interact with databases.
*   [_SQLAlchemy-Utils_](https://pypi.org/project/SQLAlchemy-Utils/) — Provides various utility functions for SQLAlchemy.
*   [_sqlacodegen_](https://github.com/agronholm/sqlacodegen) — A tool that reads the structure of an existing database and generates the appropriate SQLAlchemy model code.
*   [_PyMySQL_](https://pypi.org/project/PyMySQL/) — Used by SQLAlchemy to connect to and interact with a MySQL database, please check [this article](https://lynn-kwong.medium.com/how-to-execute-plain-sql-queries-with-sqlalchemy-627a3741fdb1) if you want to learn why PyMySQL is chosen here.
*   [_cryptography_](https://pypi.org/project/cryptography/) — Used by SQLAlchemy for authentication.
*   [_ipython_](https://pypi.org/project/ipython/) — Used to execute interactive Python code more conveniently.

Now everything is ready and we can start work with SQLAlchemy ORM.

Similar to the procedures of working with plain SQL queries with SQLAlchemy, we need to create an [Engine](https://docs.sqlalchemy.org/en/14/core/engines.html) that is the starting point for any SQLAlchemy application.

To create an Engine instance, we need to define a database URL first, which has the format of:

**dialect\[+driver\]://user:password@host:port/dbname**

*   dialect — The dialect introduced above, can be `mysql`, `postgresql`, etc.
*   driver — The name of the DBAPI used to connect to and interact with the database, which is the PyMySQL library installed above.
*   user, password, host, port, dbname — The username, password, hostname, port, and default database/schema for the target database. Please use the corresponding ones for your own case in practice.

Let’s now create an engine for our MySQL database started in a Docker container above:

[https://gist.github.com/lynnkwong/99ec7db1c23e577f3025b1f84d005e0a](https://gist.github.com/lynnkwong/99ec7db1c23e577f3025b1f84d005e0a)

`pool_size` and `pool_recycle` define how many connections (5) will be kept open in the pool, and after how long (3600 seconds) a connection will be recycled back to the pool, respectively. In this way, we can keep the number of active connections under control and won’t have stale connections that are already closed.

Unlike working with plain SQL queries, we don’t need to create a [Connection](https://docs.sqlalchemy.org/en/14/core/connections.html#sqlalchemy.engine.Connection) directly. Instead, we will create a [Session](https://docs.sqlalchemy.org/en/14/orm/session_api.html#sqlalchemy.orm.Session) that is the ORM’s “handle” to the database. A Session creates and closes Connection instances under the hood and we don’t need to worry about the details.

The preferred way to create a session is as follows:

Even though we can use the `session_factory` (which as the same suggests produces Session instances) directly, it is preferred to use the scoped session factory (called by `Session` by convention) because it produces the same `Session` instance when called in the same thread:

As we can see, the scoped session factory “magically” produces the same `Session` instance when it’s called the second time.

Besides, it should be noted that `Session` is not thread-safe and we need to create a new `Session` for each thread, which can be achieved with the `threading.local()` method:

For more info about how to write concurrent Python code with _multithreading_, please check [this article](https://lynn-kwong.medium.com/how-to-write-concurrent-python-code-with-multithreading-b24dec228c43).

Now the “handle” of SQLAlchemy is ready, we need to create an ORM model, which is just a plain Python class defining a table in our database.

With modern SQLAlchemy, an ORM model is created with the declarative system which uses a common declarative base class:

\>>> **from sqlalchemy.orm import declarative\_base**\>>> **Base = declarative\_base()**

The declarative base class `Base` works as a registry and maintains a catalog of classes and tables created with it. There should normally be only one declarative base class in all commonly imported modules. This declarative base class should be inherited by all ORM classes. Importantly, ORM classes for tables with foreign key constraints must use the same base class otherwise an exception will be raised.

Let’s use the same example as the one for [plain SQL queries](https://lynn-kwong.medium.com/how-to-execute-plain-sql-queries-with-sqlalchemy-627a3741fdb1) and create an ORM class for the `product_stocks` table in the `data` schema:

We have just created an ORM class `ProductStock` which is mapped to the `product_stocks` table. This class inherits the `Base` class so it is cataloged in the metadata of the `Base` class. As you have seen, it’s quite cumbersome to create an ORM class manually. We will introduce a much more convenient way once we have created the database and table.

If you didn’t follow the tutorial for plain SQL queries, you won’t have the `data` database and `product_stocks` table present in your local MySQL server. We can create the database and table in a MySQL console, but I want to show you something different, cooler, and more Pythonic.

We will create the database with the [SQLAlchemy-Utils](https://sqlalchemy-utils.readthedocs.io/en/latest/index.html) library which provides various utility functions for SQLAlchemy:

The `db_url` is the same one that was used to create the engine. It is passed to the `create_database()` function from the _SQLAlchemy-Utils_ library to create the target database, which is `data` in this example. It should be noted that `create_database()` will raise an exception if the database to be created already exists, therefore we need to use the `database_exists()` function from the same library to check if the database already exists before creating it.

When the command above is run, the `data` schema should be created (if it’s not created yet). We can then use the magical `Base` class to create the `product_stocks` table for which an ORM class was defined above. Technically, the `metadata` of the `Base` class is used, and it will create all the tables whose ORM classes inherit this same `Base` class:

The `[MetaData.create_all()](https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.MetaData.create_all)` method creates all the tables stored in the metadata of the `Base` class. By default, tables already exist will be skipped and no exception will be raised.

When the above command is run, the `product_stocks` table should be created in the `data` schema (if it’s not created in advance).

As we have mentioned above, it’s pretty cumbersome to create an ORM class from scratch manually. If you already have the table created in advance (which is quite common in practice), you can use the [_sqlacodegen_](https://github.com/agronholm/sqlacodegen) library to generate an ORM class for the table automatically:

As a data engineer or software engineer, you should have a pretty good understanding of the SQL syntax. It will be much more natural for you to create a table and optimize the indexes in your project database in advance, and then create an ORM class for it with the _sqlacodegen_ library as shown above.

Finally, the database, table, and ORM class are all ready and we can start to perform some basic CRUD operations with the ORM syntax.

Before we get started, let’s organize the code a bit and move logically related code to separate modules so we don’t need to repeat the code. The organized code can be found in [this repo](https://github.com/lynnkwong/sqlalchemy_orm_basic).

The DB connection code will be put in a module called `[db_connection.py](https://github.com/lynnkwong/sqlalchemy_orm_basic/blob/main/db_connection.py)`:

The `Base` class and its `metadata` are put in a separate module called `[orm_base.py](https://github.com/lynnkwong/sqlalchemy_orm_basic/blob/main/orm_base.py)` so it can be used by other ORM classes as will be introduced in future tutorials:

We specify a default schema (`data`) for the `Base` class. In this way, when multiple schemas are used, we don’t need to specify a schema if the schema is `data`. This will also be introduced in more detail later.

The ORM class for the `product_stocks` table is saved in a separate module with the code for the `Base` class removed. It’s a good practice to create a separate ORM module for every individual table for better code organization. If all the ORM classes for all tables are saved in the same file, it will be difficult to read and maintain.

Let’s first **C**reate a record with ORM. As we already know, an ORM class is mapped to a table, and the instances of the class to the rows of the table. Let’s create an instance of the `ProductStock` class and persist it to the database as a row.

Notes for this code snippet:

*   An ORM class works just like a regular Python class. If you have keen eyes, you may notice that we didn’t create an `__init__()` method for the ORM class, which is created by SQLAlchemy under the hood.
*   We can use the `Session` as a context manager, so we don’t need to explicitly close the `Session` when the DB operations are completed or failed.
*   We need to add an ORM instance to the `Session` instance then call the `commit()` method to persist it to the database. If you need to add multiple ORM instances, you can call the `add_all()` method of the `Session`.

If you query the table in the MySQL console, you can see the record just inserted:

mysql> SELECT \* FROM data.product\_stocks;  
+----------+----------+-------+---------------------+  
| stock\_id | category | stock | check\_time          |  
+----------+----------+-------+---------------------+  
|        1 | Laptops  |   999 | 2022-03-20 23:04:39 |  
+----------+----------+-------+---------------------+  
1 row in set (0,00 sec)

Let’s now **R**ead the record just created. We need to call the `query()` method and chain it with the `filter()` or `filter_by()` method. Things can get pretty complex with these methods, but we will just scratch the surface here:

Notes for this code snippet:

*   We first call the `query()` method of the `Session` with the `ProductStock` class as the parameter and then call the `filter()` or `filter_by()` method to filter by the specified condition.
*   `filter()` is the native way to filter the [Query](https://docs.sqlalchemy.org/en/14/orm/query.html) by some conditions with the SQLAlchemy ORM syntax. It supports very powerful filtering syntax as will be introduced in later tutorials. For now, you just need to know that you need to specify both the class and property and must use double equal sign rather than the single equal sign as for `filter_by()`.
*   `filter_by()` is used for simple queries on the column names using regular kwargs.
*   As you see, the result of the `query()` and f`ilter()`/`filter_by()` methods can be chained together. We can chain more `filter()`/`filter_by()` methods if needed.
*   The `first()` method returns the first result from the query. If there is no result, `None` will be returned. If we want to get all the results from the query, we can use the `all()` method, which will return a list of results, or an empty list if there is no result.
*   We can access the data with the properties of the result, which is an ORM instance.

Let’s now **U**pdate this record. Let’s set the stock to 1000. To update a record, we need to find the record first and then update it, which is quite straightforward:

If you query the table in the MySQL console, you can see updated data of the record:

mysql> SELECT \* FROM data.product\_stocks;  
+----------+----------+-------+---------------------+  
| stock\_id | category | stock | check\_time          |  
+----------+----------+-------+---------------------+  
|        1 | Laptops  |  1000 | 2022-03-20 23:04:39 |  
+----------+----------+-------+---------------------+  
1 row in set (0,00 sec)

If somehow you need to use the [**_upsert_**](https://en.wiktionary.org/wiki/upsert) or `ON DUPLICATE KEY UPDATE` syntax in MySQL, you can use the `merge()` method:

mysql> SELECT \* FROM data.product\_stocks;  
+----------+----------+-------+---------------------+  
| stock\_id | category | stock | check\_time          |  
+----------+----------+-------+---------------------+  
|        1 | Laptops  |  2000 | 2022-03-20 23:04:39 |  
+----------+----------+-------+---------------------+  
1 row in set (0,00 sec)

Note that `merge()` is much slower than `add()` or `add_all()`, so only use it when it’s really needed.

Finally, let’s see how to **D**elete a record with ORM. Let’s just delete the record we’ve been working with. To delete a record, we need to call the `delete()` method on the target record and then `commit()`:

Now this record is deleted from the database:

mysql> SELECT \* FROM data.product\_stocks;  
Empty set (0,00 sec)

In this tutorial, we have introduced the fundamentals of SQLAlchemy Object Relational Mapper (ORM). More focus is put on how to really get started with ORM from scratch. You should now be more comfortable with the basic concepts such as Engine, Session, ORM, Query, etc. Some tips are also given for how to deal with ORM issues in your practical work, such as how to create a database with SQLAlchemy and how to create an ORM class from an existing table, rather than writing everything from scratch.

In later articles, we will focus on how to use SQLAlchemy ORM with practical examples, which will involve more complex searching and filtering queries. We will also introduce how to use SQLAlchemy with popular Python frameworks such as Scrapy and Flask.


[Source](https://medium.com/codex/learn-the-basics-and-get-started-with-sqlalchemy-orm-from-scratch-66c8624b069)
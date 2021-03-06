
# Building and Testing an SQLAlchemy ORM 

[Source Article](https://medium.com/codex/learn-the-basics-and-get-started-with-sqlalchemy-orm-from-scratch-66c8624b069)b




## Docker Commands to get it running on M1Mac


**Create a volume to persist the data.**
`$ docker volume create mysql8-data`

**Create the container for MySQL.**
`$ docker run --name mysql8 -d -e MYSQL_ROOT_PASSWORD=root -p 13306:3306 -v mysql8-data:/var/lib/mysql mysql:8-oracle`


**Connect to the local MySQL server in Docker.**
$ `docker exec -it mysql8 mysql -u root -proot`

**SQL Test**
`mysql> SELECT VERSION();`


**To inspect volume**
`❯ docker volume inspect mysql8-data`

RESULT:
``` bash
[
    {
        "CreatedAt": "2022-03-23T19:55:31Z",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/mysql8-data/_data",
        "Name": "mysql8-data",
        "Options": {},
        "Scope": "local"
    }
]

```

## TODO
- [ ] make a main.py to unifty and test CRUD
- [ ] separate into modules or make into a package
- [ ] potential - ar decorators easier? Does test memory and execution time





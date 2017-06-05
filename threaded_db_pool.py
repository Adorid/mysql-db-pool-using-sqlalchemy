#!/usr/bin/env python
# coding=utf-8

"""threaded database pool using sqlalchemy.

"""

from sqlalchemy import create_engine


ENGINE = None
DB_INFO = {
    "host": "127.0.0.1",
    "user": "travis",
    "passwd": "",
    "port": 3306,
    "db": "t1",
    "pool_size": 10,
}


def get_pool():
    global ENGINE    # pylint: disable=global-statement
    if not ENGINE:
        ENGINE = create_engine(
            'mysql+pymysql://',
            connect_args={
                "host": DB_INFO["host"],
                "user": DB_INFO["user"],
                "passwd": DB_INFO["passwd"],
                "port": DB_INFO["port"],
                "db": DB_INFO["db"],
                "charset": "utf8",
            },
            pool_size=DB_INFO["pool_size"],    # default pool_size is 5.
            pool_recycle=3600)
    return ENGINE


def get_cursor():
    """return a DBAPI cursor object.

    Usually you should call this from "with" statement, see example in
    ./test_db.py

    """
    return get_pool().begin()

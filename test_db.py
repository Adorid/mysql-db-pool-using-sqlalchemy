#!/usr/bin/env python
# coding=utf-8

"""
test db connection pooling
"""

from __future__ import print_function, unicode_literals

import time
import threading

from threaded_db_pool import get_cursor


def test_basic_db_operation():
    with get_cursor() as cur:
        r = cur.execute("select 1")
        assert r.fetchone()[0] == 1


def _basic_db_operation():
    with get_cursor() as cur:
        r = cur.execute("select 1")
        time.sleep(1)
        assert r.fetchone()[0] == 1


def test_concurrent_db_operation():
    start = time.time()
    tids = []
    for _ in range(10):
        tid = threading.Thread(target=_basic_db_operation, args=())
        tid.start()
        tids.append(tid)
    for tid in tids:
        tid.join()
    end = time.time()
    assert True
    assert end - start < 2

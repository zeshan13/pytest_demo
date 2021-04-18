#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 17:21
# @Author  : zeshan
# @File    : test_fixture.py
import pytest

@pytest.fixture
def login():
    print("login123")
    return "login success"


@pytest.fixture
def connect_db():
    print("connect_db")
    return "admin"


@pytest.mark.usefixtures("login")
def test_add_cart():
    print("添加购物车")


def test_2(connect_db):
    print(connect_db)
    print("添加购物车")

@pytest.fixture(autouse=True)
def test_autouser(connect_db):
    print("test_autouser.......")


@pytest.fixture(scope="function")
def test_fixture_scope():
    print("test_fixture_scope.......")

@pytest.fixture()
def test_connect_db_2():
    print("connect db.......")
    yield "connect succ"
    print("close connect db.....")
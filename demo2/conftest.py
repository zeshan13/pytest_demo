#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 12:16
# @Author  : zeshan
# @File    : conftest.py
from do_yaml import Do_YAML
import pytest
from typing import List
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

do_yaml = Do_YAML()
case_datas = do_yaml.read_yaml(file_path="./add_cases.yaml")

@pytest.fixture(params=case_datas["datas"],ids=case_datas["ids"])
def get_add_datas(request):
    return request.param

@pytest.fixture(scope="function")
def setup_and_teardown():
    print("计算开始".center(30,"*"))
    yield "计算中..."
    print("计算结束".center(30,"*"))
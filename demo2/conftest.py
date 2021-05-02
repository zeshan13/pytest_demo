#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 12:16
# @Author  : zeshan
# @File    : conftest.py
import os

import allure
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

@pytest.fixture()
def login():
    print("login".center(30,"*"))
    return "login success..."


@pytest.fixture()
def attach_html():
    allure.attach(body=r'<head></head><body>增加html内容</body>', name="attach增加html内容",
                 attachment_type=allure.attachment_type.HTML)

png_path = os.path.join(os.path.split(os.path.abspath(__file__))[0],"taobao.png")
@pytest.fixture()
def attach_png():
    allure.attach.file(source=png_path, name="attach增加PNG内容", attachment_type=allure.attachment_type.PNG)


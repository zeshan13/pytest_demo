#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 9:06
# @Author  : zeshan
# @File    : test_div.py
# pip install pytest
import pytest
# pip install pyyaml
from do_yaml import Do_YAML
from Calculator import Calculator


calc = Calculator()

do_yaml = Do_YAML()
case_datas = do_yaml.read_yaml(file_path="./div_cases.yaml")

class TestDiv:
    @pytest.mark.parametrize('a,b,expect',case_datas["datas"], ids=case_datas["ids"])
    def test_div(self, a,b,expect,setup_and_teardown):
        print("{}/{}={}".format(str(a),str(b),str(expect)))
        try:
            assert expect == calc.div(a, b)
        except ZeroDivisionError:
            print("除数不能为0")
            assert expect == "除数不能为0"

    @pytest.mark.first
    def test_div_first(self):
        print("第一个执行的用例")

    @pytest.mark.second
    def test_div_second(self):
        print("第二个执行的用例")

    @pytest.mark.last
    def test_div_last(self):
        print("最后个执行的用例")


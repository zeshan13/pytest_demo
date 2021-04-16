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
    def setup(self):
        print("开始计算".center(30,"*"))

    def teardown(self):
        print("结束计算".center(30,"*"))

    @pytest.mark.parametrize('a,b,expect',case_datas["datas"], ids=case_datas["ids"])
    def test_div(self, a,b,expect):
        print("{}/{}={}".format(str(a),str(b),str(expect)))
        try:
            assert expect == calc.div(a, b)
        except ZeroDivisionError:
            print("除数不能为0")
            assert expect == "除数不能为0"



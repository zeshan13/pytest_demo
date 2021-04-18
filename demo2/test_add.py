#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 9:06
# @Author  : zeshan
# @File    : test_add.py

# pip install allure-pytest
import allure
# pip install pytest
import pytest
# pip install pyyaml
from Calculator import Calculator

calc = Calculator()

class TestAdd:
    def test_add(self, get_add_datas,setup_and_teardown):
        print("888")
        print(get_add_datas)
        print("{}+{}={}".format(str(get_add_datas[0]),str(get_add_datas[1]),str(get_add_datas[2])))
        assert get_add_datas[2] == calc.add(get_add_datas[0], get_add_datas[1])

    @pytest.mark.parametrize('a,b,expect',[[0.1,0.2,0.3],], ids=["浮点数相加"])
    def test_add_float(self, a,b,expect,setup_and_teardown):
        print("{}+{}={}".format(str(a),str(b),str(expect)))
        assert expect == round(calc.add(a, b),2)
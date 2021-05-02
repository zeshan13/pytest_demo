#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-16 9:06
# @Author  : zeshan
# @File    : test_allure.py

# pip install allure-pytest
import allure
# pip install pytest
import pytest
# pip install pyyaml

def choose_goods():
    print("选择商品")

def add_cart():
    print("添加购物车")

def pay():
    print("支付")


def clearn_cart():
    print("清除购物车")

def collect_goods():
    print("收藏商品")

@allure.feature("功能模块-购物车功能")
class TestGoodsCart:
    @pytest.mark.smoke
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story("pay")
    # @allure.story("子功能-加购商品并支付")
    @allure.title("测试用例名称-加购商品并支付成功")
    def test_add_cart_and_pay(login,attach_html):
        with allure.step("step1：选择商品"):
            choose_goods()

        with allure.step("step2：加入购物车"):
            add_cart()

        with allure.step("step3：支付"):
            pay()

        with allure.step("断言"):
            assert 1 == 2

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("子功能-清除购物车")
    @allure.title("测试用例名称-清除购物车")
    def test_clearn_cart(login,attach_png):
        with allure.step("step1：选择商品"):
            choose_goods()

        with allure.step("step2：清除购物车"):
            clearn_cart()

        with allure.step("断言"):
            assert 1 == 1

    @allure.testcase("https://www.taobao.com/","关联用例title")
    @allure.story("子功能-购物车商品转收藏")
    @allure.title("测试用例名称-购物车商品转收藏")
    def test_collect_goods(login):
        with allure.step("step1：选择商品"):
            choose_goods()

        with allure.step("step2：收藏购物车商品"):
            collect_goods()

        with allure.step("断言"):
            assert 1 == 1


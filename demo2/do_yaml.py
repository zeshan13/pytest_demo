#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021-04-15 22:55
# @Author  : zeshan
# @File    : do_yaml.py

# pip install pyyaml
import yaml
import os
yaml_file_path = os.path.join(os.path.split(os.path.abspath(__file__))[0],"add_cases.yaml")

class Do_YAML:

    def read_yaml(self,file_path=yaml_file_path):
        with open(file_path,encoding='utf-8') as f:
            datas = yaml.safe_load(f)
        return datas


if __name__ == '__main__':
    # print(yaml_file_path)
    t = Do_YAML()
    datas = t.read_yaml(file_path='./add_cases.yaml')
    print(datas)


'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-18 10:16:03
LastEditors: kevin.z.y
LastEditTime: 2022-07-18 10:52:07
FilePath: /udantic/tests/fields/test_nop.py
Description:

Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from udantic.fields.nop import FieldNameOfPerson
from pydantic import BaseModel

class MyModel(BaseModel):
    name: FieldNameOfPerson


def test_validation():
    model = MyModel(name="Jesson Born")
    assert model
    assert model.name.last_name == "Born"
    assert model.name.first_name == "Jesson"
    assert str(model.name) == "Jesson Born"
    model = MyModel(name="Jesson-Born")
    assert model
    assert model.name.last_name == "Born"
    assert model.name.first_name == "Jesson"
    assert str(model.name) == "Jesson Born"
    model = MyModel(name="zheng,yang")
    assert model
    assert model.name.last_name == "Zheng"
    assert model.name.first_name == "Yang"
    assert str(model.name) == "Zheng,Yang"
    model = MyModel(name="郑,杨")
    assert model
    assert model.name.last_name == "郑"
    assert model.name.first_name == "杨"
    assert str(model.name) == "郑杨"
    model = MyModel(name="杨 郑")
    assert model
    assert model.name.last_name == "郑"
    assert model.name.first_name == "杨"
    assert str(model.name) == "杨 郑"
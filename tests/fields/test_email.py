'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-18 07:46:49
LastEditors: kevin.z.y
LastEditTime: 2022-07-18 08:23:39
FilePath: /udantic/tests/fields/test_email.py
Description:

Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from udantic.fields.email import FieldEmail
from pydantic import BaseModel

class MyModel(BaseModel):
    email: FieldEmail


def test_validation():
    model = MyModel(email="kevin.cn.zhengyang@gmail.com")
    assert model
    # assert model.email.name == "John or Jane Doe"
    assert model.email.name == "kevin.cn.zhengyang"
    assert model.email.email == "kevin.cn.zhengyang@gmail.com"
    model = MyModel(email="Zheng Yang <kevin.cn.zhengyang@gmail.com>")
    assert model
    assert model.email.name == "Zheng Yang"
    assert model.email.email == "kevin.cn.zhengyang@gmail.com"

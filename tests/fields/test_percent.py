'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-19 07:40:21
LastEditors: kevin.z.y
* @LastEditTime: 2022-08-01 10:59:10
FilePath: /udantic/tests/fields/test_percent.py
Description:

Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
import pytest
from udantic.fields.percent import FieldPercent
from pydantic import BaseModel


class MyModel(BaseModel):
    percent: FieldPercent(gt=0.0, lt=100.0, max_digits=9, decimal_places=6)


def test_validation():
    model = MyModel(percent=0.25)
    assert model
    assert float(model.percent) == 0.25
    model = MyModel(percent="0.25")
    assert model
    assert float(model.percent) == 0.25
    model = MyModel(percent="25.45%")
    assert model
    assert float(model.percent) == 0.2545


def test_validation_fail():
    with pytest.raises(ValueError) as e:
        model = MyModel(percent="0xab%")
    with pytest.raises(ValueError) as e:
        model = MyModel(percent=b"0xAD34")
    model = MyModel(percent=-2.5)
    assert float(model.percent) == -2.5
    with pytest.raises(ValueError) as e:
        model = MyModel(percent=-2.5)
    with pytest.raises(ValueError) as e:
        model = MyModel(percent=345.0)

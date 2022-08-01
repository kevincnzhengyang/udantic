'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-20 10:39:12
LastEditors: kevin.z.y
LastEditTime: 2022-07-20 10:53:34
FilePath: /udantic/tests/fields/test_phone.py
Description:

Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
import pytest
from udantic.fields.phone import FieldMobileNumber
from pydantic import BaseModel

class MyModel(BaseModel):
    phone: FieldMobileNumber


def test_validation():
    model = MyModel(phone="+66-969818058")
    assert model
    assert model.phone.cc == "66"
    assert model.phone.mask == "+66-*****8058"
    model = MyModel(phone="+(66)969818058")
    assert model
    assert model.phone.cc == "66"
    assert model.phone.mask == "+66-*****8058"


def test_validation_error():
    with pytest.raises(ValueError) as e:
        model = MyModel(Phone="WaterMelon")
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        model = MyModel(Phone="7389992385")
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        model = MyModel(Phone="+66969818058")
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        model = MyModel(Phone="66-969818058")
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        model = MyModel(Phone="++66-969818058")
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        model = MyModel(Phone="+66-9698-18058")
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        model = MyModel(Phone="+(66-969818058")
    assert e.value.args[0]

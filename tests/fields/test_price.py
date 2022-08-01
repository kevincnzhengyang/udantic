'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-16 12:27:28
LastEditors: kevin.z.y
LastEditTime: 2022-07-17 14:28:08
FilePath: /udantic/tests/fields/test_price.py
Description:

Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
import pytest
import orjson
from pydantic import ConstrainedDecimal, BaseModel
from udantic.fields.price import FieldPrice


class MyModel(BaseModel):
    price: FieldPrice(currency="CNY", base=1000.0, max_digits=9)


class MyModel2(BaseModel):
    price: FieldPrice(currency="CNY", base=1.0, max_digits=9)


def test_validate_float():
    model = MyModel(price="89.490")
    assert model
    # assert isinstance(model.price, FieldPrice)
    assert float(model.price) == 89.49
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"price": 89.49}).decode()
    assert model.price.to_value() == f"CNY{89.490*1000}"
    assert model.price.to_dict() == {"currency": "CNY", "base": 1000.0, "amount": 89.490}


def test_validate_symbol():
    with pytest.raises(ValueError) as e:
        model = MyModel(price="¥89.490")
    assert e.value.args[0]

    model = MyModel2(price="¥89.490")
    assert model
    assert float(model.price) == 89.49
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"price": 89.49}).decode()
    assert model.price.to_value() == "CNY89.49"
    assert model.price.to_dict() == {"currency": "CNY", "base": 1.0, "amount": 89.490}



def test_validate_currency():
    with pytest.raises(ValueError) as e:
        model = MyModel(price="CNY89.490")
    assert e.value.args[0]
    model = MyModel2(price="CNY89.490")
    assert model
    assert float(model.price) == 89.49
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"price": 89.49}).decode()
    assert model.price.to_value() == "CNY89.49"
    assert model.price.to_dict() == {"currency": "CNY", "base": 1.0, "amount": 89.490}



def test_validate_dict():
    with pytest.raises(ValueError) as e:
        model = MyModel(price={"currency": "USD", "base": 1000.0, "ammount": 89.30})
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        model = MyModel(price={"currency": "CNY", "base": 1000000.0, "ammount": 89.30})
    assert e.value.args[0]
    model = MyModel(price={"currency": "CNY", "base": 1000.0, "amount": 35.680})
    assert model
    assert float(model.price) == 35.68
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"price": 35.68}).decode()
    assert model.price.to_value() == f"CNY{35.680*1000}"
    assert model.price.to_dict() == {"currency": "CNY", "base": 1000.0, "amount": 35.680}


'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-12 18:31:51
LastEditors: kevin.z.y
LastEditTime: 2022-07-15 17:16:27
FilePath: /udantic/tests/fields/test_select.py
Description:

Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
import pytest
import orjson
from udantic.fields.select import FieldSelect
from pydantic import BaseModel


class SimpleSelect(FieldSelect):
    pass

SimpleSelect.load_defs(map={
    "苹果": "Apple",
    "香蕉": "Banana",
    "桃子": "Peach",
})


class MyModel(BaseModel):
    select: SimpleSelect


def test_load_failed():
    with pytest.raises(TypeError) as e:
        SimpleSelect.load_defs(map={"EPROM": "1", "DRAM": "2", "MCU": "1"})
    assert e.value.args[0]


def test_select_validation():
    for option in ["苹果", "香蕉", "桃子"]:
        assert option in list(SimpleSelect._FieldSelect__tv_dict.keys())
    for option in ["Apple", "Banana", "Peach"]:
        assert option in list(SimpleSelect._FieldSelect__vt_dict.keys())

    model = MyModel(select = SimpleSelect("桃子"))
    assert model
    assert str(model.select) == "桃子"
    assert model.select.to_value() == "Peach"
    assert isinstance(model.select, str)
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"select": "桃子"}).decode()


def test_select_validation_fail():
    with pytest.raises(ValueError) as e:
        model = MyModel(select = SimpleSelect("WaterMelon"))
    assert e.value.args[0]


def test_select_from():
    model = MyModel(select = SimpleSelect.from_value("Apple"))
    assert model
    assert str(model.select) == "苹果"
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"select": "苹果"}).decode()

'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-12 18:32:04
LastEditors: kevin.z.y
LastEditTime: 2022-07-15 17:16:47
FilePath: /udantic/tests/fields/test_multiselect.py
Description:

Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
import pytest
import orjson
from udantic.fields.multiselect import FieldMultiSelect
from pydantic import BaseModel


class MultiSelect(FieldMultiSelect):
    pass

MultiSelect.load_defs(["厚饼", "加辣", "分装", "加芝士", "外带"])


class MyModel(BaseModel):
    select: MultiSelect


def test_select_validation():
    model = MyModel(select = MultiSelect("加辣:外带"))
    assert model
    assert str(model.select) == "加辣:外带"
    assert model.select.to_value() == "18"
    assert isinstance(model.select, str)
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"select": "加辣:外带"}).decode()


def test_select_validation_fail():
    with pytest.raises(ValueError) as e:
        model = MyModel(select = MultiSelect("NoIce"))
    assert e.value.args[0]


def test_select_from():
    model = MyModel(select = MultiSelect.from_value("7"))
    assert model
    assert str(model.select) == "厚饼:加辣:分装"
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"select": "厚饼:加辣:分装"}).decode()

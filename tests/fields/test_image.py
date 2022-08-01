#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-07-26 22:13:37
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-08-01 10:49:49
* @FilePath    : /udantic/tests/fields/test_image.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
import pytest
from udantic.fields.image import FieldImage
from pydantic import BaseModel

class MyModel(BaseModel):
    image: FieldImage


def test_validation():
    model = MyModel(image="data:image/png;base64,AAABAAYAICAAAAEACACoCAAAZgAAA")
    assert model
    assert model.image.image_format == "png"
    assert str(model.image) == "data:image/png;base64,AAABAAYAICAAAAEACACoCAAAZgAAA"


def test_validation_fail():
    with pytest.raises(ValueError) as e:
        model = MyModel(image="data:image/png; base64 ,AAABAAYAICAAAAEACACoCAAAZgAAA")
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        model = MyModel(image="data:video/png;base64,AAABAAYAICAAAAEACACoCAAAZgAAA")
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        model = MyModel(image="base64,AAABAAYAICAAAAEACACoCAAAZgAAA")
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        model = MyModel(image="image/png;base64,AAABAAYAICAAAAEACACoCAAAZgAAA")
    assert e.value.args[0]
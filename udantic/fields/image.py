#-*-coding:UTF-8-*-
'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-07-26 20:33:38
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-07-26 22:13:07
* @FilePath    : /udantic/udantic/fields/image.py
* @Description :
base64 encoded string for image
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from typing import Any, ClassVar
from pydantic.utils import Representation
from pydantic.validators import (str_validator,
                                 constr_strip_whitespace)


class FieldImage(str):
    """
    data:image/png;base64,AAABAAYAICAAAAEACACoCAAAZgAAA......
    """
    strip_whitespace = True
    min_length = 1
    max_length = 2**16
    image_format: str

    def __init__(self, base64: str):
        self.image_format = base64[base64.find("/")+1:base64.find(";")]

    @classmethod
    def __get_validators__(cls) -> 'CallableGenerator':
        yield str_validator
        yield constr_strip_whitespace
        yield cls.validate_base64
        yield cls

    @classmethod
    def validate_base64(cls, base64: str) -> str:
        contents = base64.split(",", 1)
        if not contents[0].endswith("base64"):
            raise ValueError(f"image not encoded with base64")
        if not contents[0].startswith("data:image/"):
            raise ValueError(f"not image data")
        return base64


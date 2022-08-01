'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-16 08:15:28
LastEditors: kevin.z.y
* @LastEditTime: 2022-07-26 21:01:24
FilePath: /udantic/udantic/fields/reference.py
Description:
reference to an internal object
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from typing import Any, ClassVar
from pydantic.utils import Representation
from pydantic.validators import (str_validator,
                                 constr_strip_whitespace)


class FieldReference(str):
    strip_whitespace: ClassVar[bool] = True
    models: str
    object: str

    def __init__(self, reference: str):
        contents = reference.split(".")
        self.models = ".".join(contents[:-2])
        self.object = contents[-1]

    @classmethod
    def __get_validators__(cls) -> 'CallableGenerator':
        yield str_validator
        yield constr_strip_whitespace
        yield cls.validate_refers
        yield cls

    @classmethod
    def validate_refers(cls, reference: str) -> str:
        # TODO validate the format of reference
        return reference

    def load(self) -> object:
        import importlib
        m = importlib.import_module(self.models)
        return getattr(m, self.object)



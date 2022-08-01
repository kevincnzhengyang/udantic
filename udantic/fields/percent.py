'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-17 20:46:14
LastEditors: kevin.z.y
LastEditTime: 2022-07-19 08:09:56
FilePath: /udantic/udantic/fields/percent.py
Description:
percentage
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from typing import TYPE_CHECKING, Any, Dict
from pydantic import ConstrainedDecimal
from pydantic.types import ConstrainedNumberMeta
from udantic.fields.utils import is_float


if TYPE_CHECKING:
    FieldPercent = dict
else:

    class _FieldPercent(ConstrainedDecimal):
        """
        FieldPrice can be:
            - int, float based 1
            - str, folloing format works:
                - int or float as str, based 1
                - symbol % ended with int or float as str based 0.01
        """
        @classmethod
        def __get_validators__(cls) -> 'CallableGenerator':
            # one or more validators may be yielded which will be called in the
            # order to validate the input, each validator will receive as an input
            # the value returned from the previous validator
            yield cls.validate
            return ConstrainedDecimal.__get_validators__()

        @classmethod
        def validate(cls, t: Any):
            if isinstance(t, ConstrainedDecimal) or \
                isinstance(t, int) or isinstance(t, float):
                return cls(t)
            if not isinstance(t, str):
                raise TypeError(f"{t} can't be treated as Percent")
            pstr = str(t).strip()
            if is_float(pstr):
                return cls(float(pstr))
            elif pstr[-1] == "%" and is_float(pstr[0:-2]):
                return cls(float(pstr[0:-1]) * 0.01)
            else:
                raise TypeError(f"{t} unkown format of Percent")

        def __repr__(self):
            return f'{type(self)}({super().__repr__()})'


    class FieldPercent(type):
        def __new__(cls, *,
                    gt: ConstrainedDecimal = None,  ge: ConstrainedDecimal = None,
                    lt: ConstrainedDecimal = None, le: ConstrainedDecimal = None,
                    max_digits: int = None, decimal_places: int = None):
            namespace = dict(
                gt=gt, ge=ge, lt=lt, le=le, max_digits=max_digits, decimal_places=decimal_places
            )
            return type('PercentValue', (_FieldPercent,), namespace)

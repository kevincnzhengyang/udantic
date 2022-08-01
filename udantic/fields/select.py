'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-12 15:25:00
LastEditors: kevin.z.y
LastEditTime: 2022-07-18 08:13:05
FilePath: /udantic/udantic/fields/select.py
Description:
Select Field Type
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''

from typing import TYPE_CHECKING, Dict
from abc import ABC

if TYPE_CHECKING:
    FieldSelect = str
else:

    class FieldSelect(ABC, str):
        """
        Select Field parses a series of str pairs (value<->title) to get two dicts:
        dict(title, value) and dict(value, title). The title is used in UI, and the
        value is used in db and server.

        """
        __tv_dict: Dict[str, str] = None
        __vt_dict: Dict[str, str] = None

        @classmethod
        def __get_validators__(cls) -> 'CallableGenerator':
            # one or more validators may be yielded which will be called in the
            # order to validate the input, each validator will receive as an input
            # the value returned from the previous validator
            yield cls.validate

        @classmethod
        def load_defs(cls, map: dict) -> None :
            if len(set(map.keys())) != len(set(map.values())):
                raise TypeError(f'{cls} defs invalid for {set(map.keys())}<->{set(map.values())}')
            cls.__tv_dict = map
            # values and keys may result in different order so unexpected result of zip occurs
            # cls.__vt_dict = dict(zip(set(map.values()), set(map.keys())))
            cls.__vt_dict = {v: k for k, v in map.items()}

        @classmethod
        def validate(cls, t: str):
            if not cls.__tv_dict:
                raise TypeError(f'{cls} definition not loaded')
            if not t in cls.__tv_dict.keys():
                raise ValueError(f'{t} not in {cls} range {cls.__tv_dict.keys()}')
            return cls(t)

        @classmethod
        def from_value(cls, v: str) -> object:
            if not cls.__vt_dict:
                raise TypeError(f'{cls} definition not loaded')
            if not v in cls.__vt_dict.keys():
                raise ValueError(f'{v} not in {cls} range {cls.__vt_dict.keys()}')
            return cls(cls.__vt_dict[v])

        def __repr__(self):
            return f'{type(self)}({super().__repr__()})'

        def to_value(self) -> str:
            return self.__tv_dict[str(self)]

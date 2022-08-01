'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-12 16:38:01
LastEditors: kevin.z.y
LastEditTime: 2022-07-18 08:13:22
FilePath: /udantic/udantic/fields/multiselect.py
Description:
Multiple Select Field Type
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''

from typing import TYPE_CHECKING, List
from abc import ABC

if TYPE_CHECKING:
    FieldMultiSelect = str
else:

    class FieldMultiSelect(ABC, str):
        """
        Multiple Select Field parses a list of title not more than 63 items.

        If multiple select made, 'option1:option2:option3...' would presented.
        """
        __title_list: List[str] = None

        @classmethod
        def __get_validators__(cls) -> 'CallableGenerator':
            # one or more validators may be yielded which will be called in the
            # order to validate the input, each validator will receive as an input
            # the value returned from the previous validator
            yield cls.validate

        @classmethod
        def load_defs(cls, range: List[str]) -> None:
            if len(range) > 63 or len(range) == 0:
                raise TypeError(f'{cls} defs invalid for range length')

            for option in range:
                if ":" in option:
                    raise TypeError(f'{cls} defs invalid for ":" in option {option}')
            cls.__title_list = range

        @classmethod
        def validate(cls, t: str):
            if not cls.__title_list:
                raise TypeError(f'{cls} definition not loaded')

            for option in t.split(":"):
                if not option in cls.__title_list:
                    raise ValueError(f'{option} not in {cls} range {cls.__title_list}')
            return cls(t)

        @classmethod
        def from_value(cls, v: str) -> object:
            if not cls.__title_list:
                raise TypeError(f'{cls} definition not loaded')
            if int(v) <= 0:
                raise ValueError(f"{cls} can't accetp value {v}")
            binstr = bin(int(v))[2:][::-1]
            i = 0
            options = []
            while (i < len(binstr) + 1):
                i = binstr.find('1', i)
                if -1 == i:
                    break
                else:
                    options.append(cls.__title_list[i])
                    i += 1
            return cls(':'.join(options))

        def __repr__(self):
            return f'{type(self)}({super().__repr__()})'

        def to_value(self) -> str:
            value = 0
            print(self.__title_list)
            for option in str(self).split(":"):
                value += 1 << self.__title_list.index(option)
            return str(value)

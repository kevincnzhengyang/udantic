'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-17 20:42:11
LastEditors: kevin.z.y
LastEditTime: 2022-07-18 10:49:16
FilePath: /udantic/udantic/fields/nop.py
Description:
name of a person
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from typing import Any
from pydantic.utils import Representation
from pydantic.validators import str_validator


class FieldNameOfPerson(Representation):
    __slots__ = "first_name", "last_name", "middle_name", "in_east"

    def __init__(self, first_name: str, last_name: str,
                 middle_name: str = "", in_east: bool = False):
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.in_east = in_east

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, str):
            return f"{self.first_name} {self.middle_name} {self.last_name}" == str(other)
        else:
            return isinstance(other, FieldNameOfPerson) and (
                self.first_name, self.middle_name, self.last_name) == (
                    other.first_name, other.middle_name, other.last_name)

    @classmethod
    def __get_validators__(cls) -> 'CallableGenerator':
        yield cls.validate

    @classmethod
    def validate(cls, value: Any) -> 'FieldNameOfPerson':
        if value.__class__ == cls:
            return value
        value = str_validator(value)
        if -1 == value.find(","):
            vlist = value.translate(str.maketrans({
                "*": " ", ".": " ", "|": " ", "-": " "})).split(" ")
            in_east = False
        else:
            # last_name is the first word if , in use
            vlist = value.split(",")
            vlist.reverse()
            in_east = True
        if len(vlist) < 2:
            raise ValueError(f"{value} don't have first_name and last_name")
        return cls(vlist[0].title(), vlist[-1].title(),
                   " ".join(vlist[1:-2].title() if len(vlist)> 2 else ""),
                   in_east)

    def __str__(self) -> str:
        if not self.in_east:
            return f'{self.first_name} {self.middle_name} {self.last_name}' \
                if self.middle_name != "" else f'{self.first_name} {self.last_name}'
        else:
            if ord(self.last_name[0]) > 255:
                return f'{self.last_name}{self.middle_name}{self.first_name}' \
                    if self.middle_name != "" else f'{self.last_name}{self.first_name}'
            else:
                return f'{self.last_name},{self.middle_name},{self.first_name}' \
                    if self.middle_name != "" else f'{self.last_name},{self.first_name}'

'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-18 07:31:41
LastEditors: kevin.z.y
* @LastEditTime: 2022-07-26 20:45:30
FilePath: /udantic/udantic/fields/phone.py
Description:
phone number
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from typing import ClassVar
from pydantic.validators import (str_validator,
                                 constr_strip_whitespace,
                                 constr_length_validator)


class FieldMobileNumber(str):
    """
        Regarding to MSISDN format, Mobile Number is built up as:
                CC(Country Code) + NDC(National Destination Code) + SN(Subscriber Number)
        While people normally use NDC+SN as MIN(Mobile Identification Number) to identify a moble.
        Mobile Number accept str contains mobile subscriber number as following:
        - +CC-NSN like +66-969818058
        - +(CC)NSN like +(66)969818058
    """
    strip_whitespace: ClassVar[bool] = True
    min_length: ClassVar[int] = 12  # 10+2
    max_length: ClassVar[int] = 17  # 15+2
    cc: str

    # only +CC-NSN in use
    def __init__(self, msisdn: str):
        self.cc = msisdn[1:msisdn.find("-")]

    @classmethod
    def __get_validators__(cls) -> 'CallableGenerator':
        yield str_validator
        yield constr_strip_whitespace
        yield constr_length_validator
        yield cls.validate_digits
        yield cls

    @property
    def mask(self) -> str:
        num_masked = len(self) - (len(self.cc)+2+4)  # len(cc) + len(last4) + 2
        return f'+{self.cc}-{"*" * num_masked}{self[-4:]}'

    @classmethod
    def validate_digits(cls, msisdn: str) -> str:
        msisdn = msisdn.translate(str.maketrans({"(": "", ")": "-"}))
        if not msisdn.replace("+", "", 1).replace("-", "", 1).isdigit():
            raise ValueError(f"{msisdn} is not msisdn")
        return msisdn

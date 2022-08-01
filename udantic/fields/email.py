'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-18 07:31:28
LastEditors: kevin.z.y
LastEditTime: 2022-07-18 08:22:57
FilePath: /udantic/udantic/fields/email.py
Description:
email information
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from typing import Union
from pydantic.networks import import_email_validator
from pydantic.validators import str_validator
from pydantic import NameEmail

FieldEmail = NameEmail

# class FieldEmail(NameEmail):
#     @classmethod
#     def validate(cls, t: str) -> Union[str, NameEmail]:
#         if t.find("<") != -1 and t.find(">") != -1:
#             return NameEmail.validate(t)
#         else:
#             return NameEmail.validate(f"John or Jane Doe<{t}>")



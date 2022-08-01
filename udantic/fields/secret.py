'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-18 08:27:05
LastEditors: kevin.z.y
LastEditTime: 2022-07-18 10:54:13
FilePath: /udantic/udantic/fields/secret.py
Description:
password or other secret text
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from pydantic import SecretStr

FieldSecret = SecretStr
#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-07-26 15:41:50
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-07-27 17:43:20
* @FilePath    : /udantic/udantic/fields/uuid.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from typing import Union
from pydantic import UUID1, UUID3, UUID4, UUID5

FieldUUID = Union[UUID1, UUID3, UUID4, UUID5]

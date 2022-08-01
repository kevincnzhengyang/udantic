'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-19 07:15:41
LastEditors: kevin.z.y
LastEditTime: 2022-07-19 07:15:55
FilePath: /udantic/udantic/fields/utils.py
Description:
utilities
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''


def is_float(str):
    try:
        # 'NaN' exceptional case
        if str=='NaN':
            return False
        float(str)
        return True
    except ValueError:
        return False

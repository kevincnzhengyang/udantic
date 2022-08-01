'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-17 20:43:59
LastEditors: kevin.z.y
LastEditTime: 2022-07-17 21:52:31
FilePath: /udantic/udantic/fields/color.py
Description:
FieldColor for color
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from pydantic.color import Color

"""
Colors can be defined via:

name (e.g. "Black", "azure")
hexadecimal value (e.g. "0x000", "#FFFFFF", "7fffd4")
RGB/RGBA tuples (e.g. (255, 255, 255), (255, 255, 255, 0.5))
RGB/RGBA strings (e.g. "rgb(255, 255, 255)", "rgba(255, 255, 255, 0.5)")
HSL strings (e.g. "hsl(270, 60%, 70%)", "hsl(270, 60%, 70%, .5)")
"""
FieldColor = Color

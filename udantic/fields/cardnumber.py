'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-17 20:42:43
LastEditors: kevin.z.y
LastEditTime: 2022-07-18 07:43:37
FilePath: /udantic/udantic/fields/cardnumber.py
Description:
Card Number for payment
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from pydantic import PaymentCardNumber


"""
https://en.wikipedia.org/wiki/Payment_card
"""
FieldCardNumber = PaymentCardNumber

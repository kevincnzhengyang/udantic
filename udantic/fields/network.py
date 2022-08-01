#-*-coding:UTF-8-*-


'''
* @Author      : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @Date        : 2022-07-27 17:43:49
* @LastEditors : kevin.z.y <kevin.cn.zhengyang@gmail.com>
* @LastEditTime: 2022-07-27 17:49:12
* @FilePath    : /udantic/udantic/fields/network.py
* @Description :
* @Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from pydantic import IPvAnyAddress, IPvAnyInterface, IPvAnyNetwork

FieldIPAddress = IPvAnyAddress
FieldIPInterface = IPvAnyInterface
FieldIPNetwork = IPvAnyNetwork

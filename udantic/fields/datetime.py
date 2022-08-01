'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-15 09:52:42
LastEditors: kevin.z.y
LastEditTime: 2022-07-16 09:31:30
FilePath: /udantic/udantic/fields/datetime.py
Description: date and time field types

Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from typing import TYPE_CHECKING

import datetime as dt
import pydantic as pdt
from pydantic.datetime_parse import (
    parse_date, parse_datetime,
    parse_time, parse_duration)


if TYPE_CHECKING:
    FieldAnyDate = dt.date
    FieldAnyTime = dt.time
    FieldAnyDatetime = dt.datetime
    FieldDuration = dt.timedelta
    FieldPastDate = dt.date
    FieldFutureDate = dt.date
else:

    # class FieldAnyDate(dt.date):
    #     @classmethod
    #     def __get_validators__(cls) -> 'CallableGenerator':
    #         yield parse_date

    # class FieldAnyTime(dt.time):
    #     @classmethod
    #     def __get_validators__(cls) -> 'CallableGenerator':
    #         yield parse_time

    # class FieldAnyDatetime(dt.datetime):
    #     @classmethod
    #     def __get_validators__(cls) -> 'CallableGenerator':
    #         yield parse_datetime

    # class FieldDuration(dt.timedelta):
    #     @classmethod
    #     def __get_validators__(cls) -> 'CallableGenerator':
    #         yield parse_duration

    FieldAnyDate = dt.date
    """
        FieldAnyDate can be:
        - date, existing date object
        - int or float, see datetime
        - str, following formats work:
            - YYYY-MM-DD
            - int or float, see datetime
    """

    FieldAnyTime = dt.time
    """
        FieldAnyTime can be:
        - time, existing time object
        - str, following formats work:
            - HH:MM[:SS[.ffffff]][Z or [±]HH[:]MM]]]
    """

    FieldAnyDatetime = dt.datetime
    """
        FieldAnyDatetime can be:
        - datetime, existing datetime object
        - int or float, assumed as Unix time, i.e. seconds (if >= -2e10 or <= 2e10) or milliseconds (if < -2e10or > 2e10) since 1 January 1970
        - str, following formats work:
            - YYYY-MM-DD[T]HH:MM[:SS[.ffffff]][Z or [±]HH[:]MM]]]
            - int or float as a string (assumed as Unix time)
    """

    FieldDuration = dt.timedelta
    """
        FieldDurration can be:
        - timedelta, existing timedelta object
        - int or float, assumed as seconds
        - str, following formats work:
            - [-][DD ][HH:MM]SS[.ffffff]
            - [±]P[DD]DT[HH]H[MM]M[SS]S (ISO 8601 format for timedelta)
    """

    FieldPastDate = pdt.PastDate

    FieldFutureDate = pdt.FutureDate

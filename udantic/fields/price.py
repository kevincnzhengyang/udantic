'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-16 08:18:12
LastEditors: kevin.z.y
LastEditTime: 2022-07-19 07:16:30
FilePath: /udantic/udantic/fields/price.py
Description:
Price Field include currency and amount information
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from typing import TYPE_CHECKING, Literal, Any
from pydantic import ConstrainedDecimal
from udantic.fields.utils import is_float


if TYPE_CHECKING:
    FieldPrice = dict
else:
    _currency = [
        "AUD", "CAD", "CHF", "CNY", "EUR", "GBP",
        "INR", "JPY", "HKD", "KRW", "RUB", "SGD",
        "THB", "TWD", "USD", "VND"] # ISO4217


    _currency_symbols = {
        "$": "USD", "£": "GBP", "€": "EUR", "₩": "KRW",
        "¥": "CNY", "฿": "THB"}

    class _FieldPrice(ConstrainedDecimal):
        """
        FieldPrice can be:
            - int, float in this case "USD" will be the currency
            - dict with "currency", "base" and "amount"
            - str, folloing format works:
                - int or float as str, in this case "USD" will be the currency
                - symbol like $, ¥, €, etc followed with int or float as str
                - USD|HKD|...|etc followed with int or float as str
        """
        # Currency = Literal[
        #     "AUD", "CAD", "CHF", "CNY", "EUR", "GBP",
        #     "INR", "JPY", "HKD", "KRW", "RUB", "SGD",
        #     "THB", "TWD", "USD", "VND"] # ISO4217

        currency: Literal[_currency]
        base: float

        @classmethod
        def __get_validators__(cls) -> 'CallableGenerator':
            # one or more validators may be yielded which will be called in the
            # order to validate the input, each validator will receive as an input
            # the value returned from the previous validator
            yield cls.validate
            return ConstrainedDecimal.__get_validators__()

        @classmethod
        def validate(cls, t: Any):
            if isinstance(t, ConstrainedDecimal) or \
                isinstance(t, int) or isinstance(t, float):
                return cls(t)
            if isinstance(t, dict):
                if "amount" not in t.keys():
                    raise ValueError(f"'amount' not in keys of {t}")
                if t.get('currency', 'USD') != cls.currency:
                    raise ValueError(f"currency not matched {t.get('currency', 'USD')} <> {cls.currency}")
                if t.get('base', 1.0) != cls.base:
                    raise ValueError(f"base not matched {t.get('base', 1.0)} <> {cls.base}")
                return cls(t['amount'])
            if not isinstance(t, str):
                raise TypeError(f"{t} can't be treated as Price")
            pstr = str(t).strip().upper()

            if pstr[0] in _currency_symbols.keys():
                if _currency_symbols[pstr[0]] != cls.currency:
                    raise ValueError(f"currency not matched {pstr[0]} <> {cls.currency}")
                if 1.0 != cls.base:
                    raise ValueError(f"base is not 1.0, price should not be start with {pstr[0]}")

                return cls(pstr[1:])
            elif pstr[0:3] in _currency:
                if pstr[0:3] != cls.currency:
                    raise ValueError(f"currency not matched {pstr[0:3]} <> {cls.currency}")
                if 1.0 != cls.base:
                    raise ValueError(f"base is not 1.0, price should not be start with {pstr[0:2]}")

                return cls(pstr[3:])
            elif is_float(pstr):
                # use currency and base defined in class
                return cls(t)
            else:
                raise TypeError(f"{t} unkown format of Price")

        def __repr__(self):
            return f'{type(self)}({super().__repr__()})'

        def to_value(self) -> str:
            return f"{self.currency}{float(self)*float(self.base)}"

        def to_dict(self) -> dict:
            return {"currency": self.currency, "base": self.base,
                    "amount": float(self)}


    class FieldPrice(type):
        def __new__(cls, *, currency: str = "USD", base: float = 1.0,
                    gt: ConstrainedDecimal = None,  ge: ConstrainedDecimal = None,
                    lt: ConstrainedDecimal = None, le: ConstrainedDecimal = None,
                    max_digits: int = None, decimal_places: int = None):
            namespace = dict(currency=currency, base=base,
                gt=gt, ge=ge, lt=lt, le=le, max_digits=max_digits, decimal_places=decimal_places
            )
            return type('PriceValue', (_FieldPrice,), namespace)

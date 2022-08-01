'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-18 07:39:14
LastEditors: kevin.z.y
* @LastEditTime: 2022-08-01 10:40:37
FilePath: /udantic/tests/fields/test_cardnumber.py
Description:

Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
import pytest
from udantic.fields.cardnumber import FieldCardNumber

from datetime import date

from pydantic import BaseModel
from pydantic.types import PaymentCardBrand, PaymentCardNumber, constr


class Card(BaseModel):
    name: constr(strip_whitespace=True, min_length=1)
    number: FieldCardNumber
    exp: date

    @property
    def brand(self) -> PaymentCardBrand:
        return self.number.brand

    @property
    def expired(self) -> bool:
        return self.exp < date.today()


def test_validation_cardnumber():
    card = Card(
        name='Georg Wilhelm Friedrich Hegel',
        number='4000000000000002',
        exp=date(2043, 9, 30),
    )

    assert card.number.brand == PaymentCardBrand.visa
    assert card.number.bin == '400000'
    assert card.number.last4 == '0002'
    assert card.number.masked == '400000******0002'
    assert not card.expired


def test_validation_failed():
    # digits
    with pytest.raises(ValueError) as e:
        card = Card(
            name='Georg Wilhelm Friedrich Hegel',
            number='400000-0000000002',
            exp=date(2043, 9, 30),
        )
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        card = Card(
            name='Georg Wilhelm Friedrich Hegel',
            number='400000 0000000002',
            exp=date(2043, 9, 30),
        )
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        card = Card(
            name='Georg Wilhelm Friedrich Hegel',
            number='+4000000000000002',
            exp=date(2043, 9, 30),
        )
    assert e.value.args[0]
    with pytest.raises(ValueError) as e:
        card = Card(
            name='Georg Wilhelm Friedrich Hegel',
            number='-4000000000000002',
            exp=date(2043, 9, 30),
        )
    assert e.value.args[0]
    # brand check
    with pytest.raises(ValueError) as e:
        card = Card(
            name='Georg Wilhelm Friedrich Hegel',
            number='400000000002',
            exp=date(2043, 9, 30),
        )
    assert e.value.args[0]

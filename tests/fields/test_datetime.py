'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-15 17:05:16
LastEditors: kevin.z.y
LastEditTime: 2022-07-18 08:12:30
FilePath: /udantic/tests/fields/test_datetime.py
Description:

Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from datetime import date, time, datetime, timedelta
import pytest
import orjson
from udantic.fields.datetime import *
from pydantic import BaseModel


def test_anydate():
    class MyModel(BaseModel):
        date: FieldAnyDate


    model = MyModel(date="2022-07-15")
    assert model
    assert isinstance(model.date, date)
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"date": "2022-07-15"}).decode()

    with pytest.raises(ValueError) as e:
        model = MyModel(date = ("Hello World"))
    assert e.value.args[0]


def test_anytime():
    class MyModel(BaseModel):
        time: FieldAnyTime

    model = MyModel(time="17:15:20+08:30")
    assert model
    assert isinstance(model.time, time)
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"time": "17:15:20+08:30"}).decode()

    with pytest.raises(ValueError) as e:
        model = MyModel(time = ("Hello World"))
    assert e.value.args[0]


def test_anydatetime():
    class MyModel(BaseModel):
        time: FieldAnyDatetime

    model = MyModel(time="2022-07-15 17:15:20+08:30")
    assert model
    assert isinstance(model.time, datetime)
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"time": "2022-07-15T17:15:20+08:30"}).decode()

    model = MyModel(time="524694139563")
    assert model
    assert isinstance(model.time, datetime)
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"time": "1986-08-17T20:22:19.563000+00:00"}).decode()

    with pytest.raises(ValueError) as e:
        model = MyModel(time = ("Hello World"))
    assert e.value.args[0]


def test_duration():
    class MyModel(BaseModel):
        duration: FieldDuration

    model = MyModel(duration="-03 05:30:20")
    assert model
    assert isinstance(model.duration, timedelta)
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"duration": -239380.0}).decode()

    model = MyModel(duration="+P4DT11H38M20.035000055S")
    assert model
    assert isinstance(model.duration, timedelta)
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"duration": 387500.035}).decode()

    with pytest.raises(ValueError) as e:
        model = MyModel(time = ("Hello World"))
    assert e.value.args[0]


def test_pastdate():
    class MyModel(BaseModel):
        past: FieldPastDate

    today = datetime.today()

    yesterday = (today - timedelta(hours=24)).strftime("%Y-%m-%d")
    model = MyModel(past=yesterday)
    assert model
    assert isinstance(model.past, date)
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"past": yesterday}).decode()

    with pytest.raises(ValueError) as e:
        model = MyModel(date = today.strftime("%Y-%m-%d"))
    assert e.value.args[0]


def test_futuredate():
    class MyModel(BaseModel):
        future: FieldFutureDate

    today = datetime.today()

    tomorrow = (today + timedelta(hours=24)).strftime("%Y-%m-%d")
    model = MyModel(future=tomorrow)
    assert model
    assert isinstance(model.future, date)
    assert model.json(ensure_ascii=False).replace(" ", "") == \
        orjson.dumps({"future": tomorrow}).decode()

    with pytest.raises(ValueError) as e:
        model = MyModel(date = today.strftime("%Y-%m-%d"))
    assert e.value.args[0]

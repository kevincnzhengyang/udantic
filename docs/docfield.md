<!--
 * @Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
 * @Date: 2022-07-12 11:02:46
 * @LastEditors: kevin.z.y
 * @LastEditTime: 2022-07-16 08:20:31
 * @FilePath: /udantic/docs/docfield.md
 * @Description:
 *
 * Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
-->
# DocField
DocField provide a patch of Field Types which are user understanding friendly.

# Field Types

## Data
base: pydantic.constr

## Reference
base: pydantic.pyobject

### Link
data link between Models
base: None
should used in desinger context instead of user context

------
base: pyobject

### Dynamic Link
conditional data linke between Models
base: None
should used in desinger context instead of user context

------
base: union/depend-on/pyobject

## Check
base: bool

## Select
base: typing.Literal/typing.Dict

## Table
base: typing.Iterable/pydantic.pyobject

## Attach
base: pydantic.FilePath/pydantic.FileURL

## Attach Image
base: pydantic.FilePath/pydantic.FileURL

## Date
base: date/pydantic.PastDate/pydantic.FutureDate

## Date and Time
base: datetime/date/time/timedelta

## Barcode
base: pydantic.constr

generate bar

## Button
base: None
should used in desinger context instead of user context

## Code
base: pydantic.constr

shell, python, js, css, html, etc

## Color
base: pydantic.Color

## Column Break
base: None
should used in desinger context instead of user context

## Price
## Currency
base: pydantic.condecimal

currency and amount

## Float
base: pydantic.confloat

## Goelocation
GoeJSON
base: pydantic.Json

## HTML
base: todo

## Image
base: pydantic.constr

base64

## Int
base: pydantic.conint

## Text
base: pydantic.constr

## Markdown Editor
base: todo

## Password
base: pydantic.SecretStr/pydantic.SecretBytes

## Percent
base: todo

## Rating
base: todo
range and label

## Section Break
base: None
should used in desinger context instead of user context

## Tab Break
base: None
should used in desinger context instead of user context

## Signature
base: pydantic.conbytes

hand writing signature picture

## Table MultiSelect
base: None
should used in desinger context instead of user context

## Time
base: time/timedelta

## Duration
base: timedelta
If you don't want to track duration in terms of days or seconds, you can enable "Hide Days" and "Hide Seconds" options respectively in your Form.

## JSON
base: pydantic.Json

## Name
base: pydantic.constr

## Email
base: pydantic.EmailStr/pydantic.NameEmail

## Phone
base: pydantic.constr

## PaymentCardNumber
base: pydantic.PaymentCardNumber

## DBDsn
base: pydantic.PostgresDsn/pydantic.RedisDsn

## URL
base: pydantic.AnyUrl

## UUID
base: pydantic.UUID*

## IPAddress
base: pydantic.IPvAny*

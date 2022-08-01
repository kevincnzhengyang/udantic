'''
Author: kevin.z.y <kevin.cn.zhengyang@gmail.com>
Date: 2022-07-17 20:44:23
LastEditors: kevin.z.y
LastEditTime: 2022-07-18 09:32:10
FilePath: /udantic/udantic/docs/attach.py
Description:
attachments contains image, audio, video, file, etc.
Copyright (c) 2022 by Zheng, Yang, All Rights Reserved.
'''
from typing import Literal
from pydantic import BaseModel, FileUrl, HttpUrl, constr, Field

class DocAttach(BaseModel):
    name: str = Field(
        ...,
        title="Name",
        description="the name of attachment showed to user")
    category: Literal["Image", "Audio", "Video", "File", "Memo", "Others"] = Field(
        default="Others",
        title="Category",
        description="the category of attachment showed to user")
    format: constr(strip_whitespace=True, to_lower=True) = Field(
        None,
        title="Format",
        description="the filename extension of the original file")
    origin: FileUrl = Field(
        None,
        title="URL for details",
        description="the URL to get original attachment")
    thumbnail: HttpUrl = Field(
        None,
        title="URL for thumbnail",
        description="the URL to get thumbnail of attachment")

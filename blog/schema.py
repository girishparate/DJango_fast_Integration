from datetime import date, datetime
from typing import Any, Generic, List, Optional, Type, Union
from pydantic import BaseModel, validator


def confirm_title(value: str) -> str:
    if not value:
        raise ValueError("Please write a title.")
    return value


def confirm_text(value: str) -> str:
    if not value:
        raise ValueError("Please enter text.")
    return value

class SampleBase(BaseModel):
    title: str
    text: str
    _confirm_title = validator('title', allow_reuse=True)(confirm_title)
    _confirm_text = validator('text', allow_reuse=True)(confirm_text)


class CreateSample(SampleBase):
    "..."

class UpdateSample(SampleBase):
    "something"

class SampleOut(SampleBase):
    title: str
    text: str

    class Config:
        orm_mode = True

class SampleListOut(BaseModel):
    title: str
    text: str

    class Config:
        orm_mode = True



class AllSampleList(SampleBase):
    """
    Response for listing all blog posts.
    Custom for just these few fields
    """
    id: int
    draft: bool = False

    class Config:
        orm_mode = True

class SingleSample(SampleBase):
		"""
		Response for a blog post.
		"""

		id: int
		slug: str
		view_count: int
		draft: bool = False
		publish: date
		description: Optional[str] = None
		content: Optional[str] = ...
		read_time: int
		category: SampleOut

		class Config:
			orm_mode = True
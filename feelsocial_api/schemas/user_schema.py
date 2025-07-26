from datetime import datetime

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    username: str
    email: EmailStr
    banned: bool
    confirmed_email: bool
    banned_date: datetime
    created_at: datetime
    updated_at: datetime

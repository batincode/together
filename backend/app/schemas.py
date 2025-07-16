from pydantic import BaseModel
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    bio: Optional[str] = ''

class UserRead(BaseModel):
    id: int
    username: str
    bio: Optional[str]

    class Config:
        orm_mode = True

class ProjectCreate(BaseModel):
    title: str
    description: Optional[str] = ''
    language: Optional[str] = ''

class ProjectRead(BaseModel):
    id: int
    title: str
    description: Optional[str]
    language: Optional[str]

    class Config:
        orm_mode = True

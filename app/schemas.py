from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    n8n_link: Optional[str] = None
    
    class Config:
        from_attributes = True

class ProjectBase(BaseModel):
    name: str
    scope: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    value: Optional[float] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    id: int
    tap_generated: bool
    created_at: datetime
    owner_id: int

    class Config:
        from_attributes = True

class ChatMessage(BaseModel):
    role: str
    content: str

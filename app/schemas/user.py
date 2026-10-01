from pydantic import BaseModel,Field,EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    name: str =Field(...,min_length=2,max_length=100)
    email: EmailStr

class UserResponse(BaseModel):
    id: str
    nome: str
    email: EmailStr
    created_at: datetime
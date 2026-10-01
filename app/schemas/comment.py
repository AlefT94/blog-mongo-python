from datetime import datetime
from pydantic import BaseModel,Field

class CommentCreate(BaseModel):
    user_id: str = Field(...,min_length=1)
    text: str = Field(...,min_length=1, max_length=600)

class CommentResponse(BaseModel):
    id: str
    user_id: str
    user_name_snapshot: str
    text: str
    created_at: datetime
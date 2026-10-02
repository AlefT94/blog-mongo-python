from pydantic import BaseModel,Field
from datetime import datetime

from app.schemas.comment import CommentResponse

class ArticleCreate(BaseModel):
    title: str = Field(...,min_length=1)
    text: str = Field(...,min_length=1)
    author_id: str =Field(...,min_length=1)
    tags: list = []

class ArticleResponse(BaseModel):
    id: str
    title: str
    text: str
    author_id: str
    author_name_snapshot: str
    tags: list[str] = []
    comments: list[CommentResponse] = []
    created_at: datetime
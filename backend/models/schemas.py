from pydantic import BaseModel, HttpUrl
from typing import Optional


class LoadUrlRequest(BaseModel):
    source_type: str
    url: Optional[HttpUrl] = None


class QueryRequest(BaseModel):
    query: str
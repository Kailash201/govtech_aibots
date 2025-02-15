from pydantic import BaseModel
from typing import List


class WebsiteReq(BaseModel):
    urls: List[str]

class QueryReq(BaseModel):
    query: str
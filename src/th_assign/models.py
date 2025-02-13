from beanie import Document

from pydantic import BaseModel
from typing import List

class Query(BaseModel):
    content: str


class AgentModel(Document):
    name: str
    files: List[str]
    websites: List[str]
    extracted_test_files: str
    extracted_test_websites: str

    class Settings:
        name = "agents"
from uuid import UUID, uuid4
from beanie import Document

from fastapi import UploadFile
from pydantic import BaseModel, Field
from typing import List, Any

class Query(BaseModel):
    content: str


class FileDocument(Document):
    name: str
    content: bytes
    content_type: str


class AgentModel(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    files: List[FileDocument] | None
    websites: List[str] | None


    class Settings:
        name = "agents"



    
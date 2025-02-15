from beanie import Document
from pydantic import Field
from typing import List
from uuid import UUID, uuid4

class FileDocument(Document):
    name: str
    content: bytes
    content_type: str
    extracted_content: str | None


class WebsiteDocument(Document):
    url: str
    extracted_content: str | None


class AgentModel(Document):
    id: UUID = Field(default_factory=uuid4)
    name: str
    files: List[FileDocument] | None
    websites: List[WebsiteDocument] | None


    class Settings:
        name = "agents"
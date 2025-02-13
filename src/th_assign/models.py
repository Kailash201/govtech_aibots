from beanie import Document

from pydantic import BaseModel


class Query(BaseModel):
    message: str


class AgentModel(Document):
    id: int
    name: str

    class Settings:
        name = "agents"
from beanie import Document

class AgentModel(Document):
    id: int
    name: str

    class Settings:
        name = "agents"
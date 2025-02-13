from beanie import Document

class AgentModel(Document):
    name: str

    class Settings:
        name = "agents"
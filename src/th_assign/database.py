from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from .models import AgentModel, FileDocument


class Database:
    
    @staticmethod
    async def init():
        client = AsyncIOMotorClient("mongodb://localhost:27017")
        await init_beanie(
            database=client.govtech, document_models=[AgentModel, FileDocument]
        )


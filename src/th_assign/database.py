from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from .models.beanieModels import AgentModel, FileDocument, WebsiteDocument


class Database:
    
    @staticmethod
    async def init():
        client = AsyncIOMotorClient("mongodb://localhost:27017")
        await init_beanie(
            database=client.govtech, document_models=[AgentModel, FileDocument, WebsiteDocument]
        )


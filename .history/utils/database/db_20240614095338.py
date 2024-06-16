from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config.settings import settings


async def init() -> None:
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    await init_beanie(client.suggestion, document_models=[])
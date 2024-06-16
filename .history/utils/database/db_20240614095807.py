from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from config.


async def init_db() -> None:
    client = AsyncIOMotorClient(settings.MONGODB_URL)
    await init_beanie(client.suggestion_box_db, document_models=[])
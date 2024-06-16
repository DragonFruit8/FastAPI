from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient
from config.

async def init() -> None:
    client = AsyncIOMotorClient()
    await init_beanie()
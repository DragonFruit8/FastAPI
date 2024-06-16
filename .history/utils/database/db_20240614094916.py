from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient


async def init() -> None:
    client = AsyncIOMotorClient("mongodb://localhost:27017")
    await init_beanie()
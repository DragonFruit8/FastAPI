from beanie import init_beanie

async def init() -> None:
    await init_beanie(database_url="mongodb://localhost:27017", database_name="test")
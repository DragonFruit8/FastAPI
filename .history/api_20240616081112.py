from fastapi import FastAPI
from routes.users import router as user_router
from routes.companies import router as

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(user_router)
    return app

app = create_app()

@app.on_event("startup")
async def startup_event():
    from utils.database.db import init_db
    await init_db()

@app.get("/")
async def read_root():
    return {"msg": "World"}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", reload=True)
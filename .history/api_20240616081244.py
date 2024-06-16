from fastapi import FastAPI
from routes import users, companies

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(users.router)
    app.include_router()
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
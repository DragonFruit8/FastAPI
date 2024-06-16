from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI()
    return app

app = create_app()

@app.on_event("startup")
async def startup_event():
    from utils.database.db import init_db
    await init_db()

@app.get("/")
async def read_root():
    return {msg: "World"}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", reload=True)
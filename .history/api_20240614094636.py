from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI()
    return app

@app.get("/")
async def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", reload=True)
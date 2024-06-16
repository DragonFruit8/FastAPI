from fastapi import FastAPI

def create_app() -> FastAPI:
    app = FastAPI()
    return app

if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("api:app", reload=True)
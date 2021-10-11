from fastapi import FastAPI

from app.config.container import Container
from app.config.settings import Settings
from app import endpoints

def create_app() -> FastAPI:
    container = Container()
    container.config.from_pydantic(Settings())
    print(Settings().dict())
    container.wire(modules=[endpoints])

    db = container.db()

    app = FastAPI()
    app.container = container
    app.include_router(endpoints.router)
    return app


app = create_app()
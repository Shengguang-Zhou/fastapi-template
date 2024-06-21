import logging

from fastapi import FastAPI

from app.provider import app_provider
from app.provider import logging_provider
from app.provider import handle_exception
from app.provider import route_provider

from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi import Depends

from safety.doc import get_current_username


def create_app() -> FastAPI:
    app = FastAPI(docs_url=None, redoc_url=None, openapi_url=None)

    register(app, logging_provider)
    register(app, app_provider)
    register(app, handle_exception)

    boot(app, route_provider)

    @app.get("/docs", include_in_schema=False)
    async def get_documentation(username: str = Depends(get_current_username)):
        return get_swagger_ui_html(openapi_url="/openapi.json",
                                   title="docs")

    @app.get("/openapi.json", include_in_schema=False)
    async def openapi(username: str = Depends(get_current_username)):
        return get_openapi(title="FastAPI",
                           version="0.1.0",
                           routes=app.routes)

    return app


def register(app, provider):
    provider.register(app)
    logging.info(provider.__name__ + ' registered')


def boot(app, provider):
    provider.boot(app)
    logging.info(provider.__name__ + ' booted')

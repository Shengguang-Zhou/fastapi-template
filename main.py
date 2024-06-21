import uvicorn
from fastapi import FastAPI

from router.router import api_router
from router.oauth import oauth_router

from initialization.init_sqlalchemy import mysql_init
from contextlib import asynccontextmanager



@asynccontextmanager
async def lifespan(app: FastAPI):
    await mysql_init()
    yield

# app = FastAPI(lifespan = lifespan)
app = FastAPI()
print(f'Database initialized:{mysql_init()}')

app.include_router(oauth_router, prefix = '/api/v1/oauth')
app.include_router(api_router, prefix = '/api/v1')






@app.get("/")
async def root():
    text = ("FASTAPI TEMPLATE FOR EUREKAI LAB")
    return text


if __name__ == "__main__":
    from config.config import settings
    if settings.ENV == 'PRODUCTION':
        uvicorn.run(app,
                    host="0.0.0.0",
                    port=settings.SERVER_PORT,
                    reload=False)

    elif settings.ENV == 'DEVELOPMENT':
        uvicorn.run('main:app',
                    host="0.0.0.0",
                    port=settings.SERVER_PORT,
                    reload=settings.DEBUG)


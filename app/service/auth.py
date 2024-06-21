from fastapi_users.authentication import (
    AuthenticationBackend,
    BearerTransport,
    CookieTransport,
    JWTStrategy,
)
from fastapi_users.authentication.strategy.db import AccessTokenDatabase, DatabaseStrategy
from fastapi import Depends

from safety.secret import SECRET, PUBLIC_KEY
from database.mysql.userDatabase import get_access_token_db
from app.model.accessToken import AccessToken





SECRET = "SECRET"


bearer_transport = BearerTransport(tokenUrl="auth/bearer/login")
cookie_transport = CookieTransport(cookie_name='learniqueauth',
                                   cookie_max_age=3600)



def get_jwt_strategy() -> JWTStrategy:
    # TODO: implement RS256 and use rs 256 for all secret
    return JWTStrategy(secret=SECRET,
                       lifetime_seconds=3600,
                       # algorithm='RS256',
                       # public_key=PUBLIC_KEY
                       )

def get_database_strategy(
        access_token_db: AccessTokenDatabase[AccessToken] = Depends(get_access_token_db),
) -> DatabaseStrategy:
    return DatabaseStrategy(access_token_db, lifetime_seconds=3600)


# TODO: implement Redis strategy
# https://fastapi-users.github.io/fastapi-users/latest/configuration/authentication/strategies/redis/


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)

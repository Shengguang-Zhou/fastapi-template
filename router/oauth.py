import uuid

from fastapi_users import FastAPIUsers

from app.model.user import User
from app.service.auth import auth_backend
from app.service.user import user_manager
from app.schema.user import UserCreate, UserRead,UserUpdate
from fastapi import APIRouter

oauth_router = APIRouter()

fastapi_users = FastAPIUsers[User, uuid.UUID](
    user_manager,
    [auth_backend],
)



# registration
oauth_router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["Auth - Registration"],
)

# login
oauth_router.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["Auth - Login JWT"],
    # description = 'Login JWT authentication'
)

# reset password
oauth_router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["Auth - Reset password"],
)

# email verification
oauth_router.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["Auth - Email verification"],
)


# manage user
oauth_router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["Auth - Users"],
)
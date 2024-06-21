import uuid
from datetime import datetime

from fastapi import Depends, Request, Response
from fastapi_users import BaseUserManager, FastAPIUsers, UUIDIDMixin
from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users import BaseUserManager, InvalidPasswordException, UUIDIDMixin

from app.model.user import User
from app.schema.user import UserCreate
from database.mysql.userDatabase import get_user_db
from safety.secret import SECRET, RESET_PASSWORD_SECRET, VERIFICATION_SECRET

from typing import Optional, Union, Dict, Any



SECRET = "SECRET"



class UserManager(UUIDIDMixin, BaseUserManager[User, uuid.UUID]):
    reset_password_token_secret = RESET_PASSWORD_SECRET
    verification_token_secret = VERIFICATION_SECRET

    async def validate_password(
            self,
            password: str,
            user: Union[UserCreate, User],
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )
        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain e-mail"
            )


    ############################################################################
    ############################# callback #####################################
    ############################################################################


    ############################# register #####################################
    async def on_after_register(self, user: User, request: Optional[Request] = None):
        # TODO: sending a marketing email in the future version
        print(f"User {user.id} has registered. \nRegistration time: {datetime.utcnow() }")



    ############################ reset password #####################################
    async def on_after_forgot_password(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        # TODO: sending email
        print(f"User {user.id} has forgot their password. Reset token: {token}. \nReset time: {datetime.utcnow()}")

    async def on_after_reset_password(self, user: User, request: Optional[Request] = None):
        # TODO: sending email
        print(f"User {user.id} has reset their password.")

    ############################## login & verification #####################################
    async def on_after_request_verify(
            self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification token: {token}.\nVerification time: {datetime.utcnow()}")

    async def on_after_verify(
            self, user: User, request: Optional[Request] = None
    ):
        print(f"User {user.id} has been verified")
    async def on_after_login(self,
                       user: User,
                       request: Optional[Request] = None,
                       response: Optional[Response] = None,):
        return (f'User {user.id} has logged in. \nLogin time: {datetime.utcnow()}')


    ############################## update #####################################
    async def on_after_update(
            self,
            user: User,
            update_dict: Dict[str, Any],
            request: Optional[Request] = None,
    ):
        print(f"User {user.id} has been updated with {update_dict}.")

    ############################## delete #####################################
    async def on_before_delete(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} is going to be deleted.\nDeletion time: {datetime.utcnow()}")

    async def on_after_delete(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} is successfully deleted.\nDeletion time: {datetime.utcnow()}")



async def user_manager(user_db: SQLAlchemyUserDatabase = Depends(get_user_db)):
    yield UserManager(user_db)






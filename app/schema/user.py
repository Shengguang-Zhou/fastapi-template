from fastapi_users import schemas
import uuid


class UserCreate(schemas.BaseUserCreate):
    '''
    user registration
    '''
    # BaseUserCreate provide followng
    # 1. email: EmailStr
    # 2. password: str
    # 3. is_active: Optional[bool] = True
    # 4. is_superuser: Optional[bool] = False
    # 5. is_verified: Optional[bool] = False
    UserName: str
    Phone: int
    UserIcon: str
    pass


class UserRead(schemas.BaseUser[uuid.UUID]):
    # BaseUser Provides following
    # 1. id: models.ID
    # 2. email: EmailStr
    # 3. is_active: bool = True
    # 4. is_superuser: bool = False
    # 5. is_verified: bool = False
    pass

class UserUpdate(schemas.BaseUserUpdate):
    # BaseUserUpdate Provides following
    # 1. email: Optional[EmailStr] = None
    # 2. password: Optional[str] = None
    # 3. is_active: Optional[bool] = None
    # 4. is_superuser: Optional[bool] = None
    # 5. is_verified: Optional[bool] = None
    UserName: str
    Phone: int
    UserIcon: str
    pass




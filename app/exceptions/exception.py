"""
框架异常类
"""


class AuthenticationError(Exception):
    """
    未认证
    """

    def __init__(self, message: str = "Unauthorized"):
        self.message = message


class AuthorizationError(Exception):
    """
    未授权
    """

    def __init__(self, message: str = "Forbidden"):
        self.message = message


class InternalServerError(Exception):
    """
        内部服务器异常
    """

    def __init__(self, message: str = "internal server error"):
        self.message = message

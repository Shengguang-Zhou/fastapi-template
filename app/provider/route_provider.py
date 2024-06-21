from router.router import api_router
from router.oauth import oauth_router


def boot(app):
    # 注册api路由[routes/docVerification.py]
    app.include_router(api_router, prefix="/api")
    app.include_router(oauth_router, prefix="/OAuth")

    # 打印路由
    if app.debug:
        for route in app.routes:
            print({'path': route.path, 'name': route.name, 'methods': route.methods})

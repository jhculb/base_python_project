class IncludeAPIRouter(object):
    def __new__(cls):
        from app.utils.routers.health_checks import router as router_health_check
        from app.utils.routers.hello_world import router as router_hello_world
        from fastapi.routing import APIRouter
        router = APIRouter()
        router.include_router(router_health_check, prefix='/api/v1', tags=['health_check'])
        router.include_router(router_hello_world, prefix='/api/v1', tags=['hello_world'])
        return router
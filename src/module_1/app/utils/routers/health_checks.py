from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from application.initializer import LoggerInstance

router = APIRouter()
logger = LoggerInstance().get_logger(__name__)


@router.get("/")
async def hello_world():
    logger.info('Hello Worldππ»')
    return JSONResponse(content={"message": "Hello World! ππ»"}, status_code=200)
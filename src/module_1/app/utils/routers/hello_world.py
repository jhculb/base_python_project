from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter

from app.utils.logger.instantiate import logger_instance
from app.utils.logger.instantiate import db_instance

_db = db_instance
router = APIRouter(prefix='/health-check')
logger = logger_instance.get_logger(__name__)


@router.get('/')
async def health_check():
    logger.info('Health Check⛑')
    await _db.insert_single_db_record({"Status": "OK"})
    return JSONResponse(content='OK⛑', status_code=200)
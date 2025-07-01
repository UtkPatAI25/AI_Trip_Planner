from fastapi import Request
from fastapi.responses import JSONResponse
from logger.logger import logger

async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "An unexpected error occurred."}
    )
    
from fastapi import APIRouter, Depends

from app.models.redis import RedisClient

router = APIRouter()


@router.post("/user-cleanup")
async def user_cleanup(
    redis_client: RedisClient = Depends(RedisClient),
    user_id: str = "u_1234",
):
    redis_conn = redis_client.get_conn()
    redis_conn.delete(user_id)
    return "Clean up done"


@router.post("/all-cleanup")
async def all_cleanup(
    redis_client: RedisClient = Depends(RedisClient),
):
    redis_conn = redis_client.get_conn()
    redis_conn.flushdb()
    return "Clean up done"


@router.get("/get-user-message")
async def get_user_message(
    redis_client: RedisClient = Depends(RedisClient),
    user_id: str = "u_1234",
):
    redis_conn = redis_client.get_conn()
    return redis_conn.lrange(user_id, 0, -1)


@router.get("/get-user-list")
async def get_user_list(
    redis_client: RedisClient = Depends(RedisClient),
):
    # This is not good code, change it to scan
    redis_conn = redis_client.get_conn()
    return redis_conn.keys("*")

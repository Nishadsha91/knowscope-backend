from fastapi import HTTPException, Header
from .jwt_handler import get_current_user


async def get_user_from_header(authorization: str = Header(...)):
    print("Authorization header received:", authorization)
    token = authorization.split(" ")[1]
    try:
        return get_current_user(token)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))
    
    
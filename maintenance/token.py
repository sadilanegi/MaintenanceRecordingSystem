from datetime import datetime, timedelta
from jose import JWTError, jwt
from . import schemas


# we run command(openssl rand -hex 32) in linux to get secret key
SECRET_KEY = "b7d7c1c2457a9c64a05b80dcf2f23f0a09cacd3f520ff8f65a12d5f769906515"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token:str,credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception




# we run command(openssl rand -hex 32) in linux to get secret key
#SECRET_KEY = "b7d7c1c2457a9c64a05b80dcf2f23f0a09cacd3f520ff8f65a12d5f769906515"
from fastapi import APIRouter
from . models import *
from .pydantic_model import Person

from passlib.context import CryptContext
from fastapi.encoders import jsonable_encoder





app = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


@app.post("/")
async def ragistration(data: Person):
    if await User.exists(phone=data.phone):
        return {"status": False, "message": "phone number already exists"}
    elif await User.exists(email=data.email):
        return {"status": False, "message": "email already exists"}
    else:
        user_obj = await User.create(email=data.email, name=data.name,
                                     phone=data.phone, password=get_password_hash(data.password))
        return  {"status": True, "message": "Ragistration complate"}
        

@app.get('/data/')
async def all_user():
    user_obj = await User.all()
    return user_obj





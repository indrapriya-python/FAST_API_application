from fastapi import APIRouter
from . models import *
from .pydantic_model import Person,User_update,User_delete

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


@app.put('/update')
async def update_user(data:User_update):
    user = await User.get(id=data.id)
    if not user:
        return {"status":False, "message":"User not found"}
    else:
        user_obj = await User.filter(id=data.id).update(name = data.name,email = data.email, phone = data.phone)
        return user_obj

@app.delete('/delete')
async def delete_user(data:User_delete):
    user = await User.filter(id=data.id).delete()
    return {"status":True, "message":"User deleted successfully"}


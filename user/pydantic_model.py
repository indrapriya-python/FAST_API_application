from pydantic import BaseModel



class Person(BaseModel):
    name:str
    email:str
    phone:int
    password:str

class User_update(BaseModel):
    id : int 
    name : str
    email: str
    phone: int

class User_delete(BaseModel):
    id : int
      
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from user import api as UserAPI


app = FastAPI()

app.include_router(UserAPI.app, tags=["api"])



register_tortoise(
    app,
    db_url="postgres://postgres:12345@127.0.0.1/test",
    modules={'models': ['user.models',]},
    generate_schemas=True,
    add_exception_handlers=True
)

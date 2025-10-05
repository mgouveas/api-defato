from fastapi import FastAPI
from http import HTTPStatus
#from fastapi.responses import HTMLResponse
from ..utils.schemas import MessageSchema, UserSchema, UserPublic


app = FastAPI()

@app.get('/', status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {
        'message': 'API On'
    }

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    pass
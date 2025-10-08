from fastapi import FastAPI, HTTPException
from http import HTTPStatus
#from fastapi.responses import HTMLResponse
from ..utils.schemas import MessageSchema, UserSchema, UserPublic, UserDB, UserList

app = FastAPI()

database = []

@app.get('/users/', status_code=HTTPStatus.OK, response_model=UserList)
def read_users():
    return {
        'users': database
    }

@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    new_user = UserDB(**user.model_dump(), id=len(database) + 1)  

    database.append(new_user)

    return new_user

@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    
    user_with_id = UserDB(**user.model_dump(), id=user_id)
    database[user_id - 1] = user_with_id

    return user_with_id
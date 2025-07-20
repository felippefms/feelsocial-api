from http import HTTPStatus

from fastapi import FastAPI

from schemas.user_schema import UserPublic, UserSchema

app = FastAPI(title='Feelsocial API')


@app.get('/', status_code=HTTPStatus.OK)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user

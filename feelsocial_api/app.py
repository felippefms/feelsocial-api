from http import HTTPStatus

from fastapi import FastAPI

from feelsocial_api.routers import users_routes
from feelsocial_api.schemas.message_schema import MessageSchema

app = FastAPI(title='Feelsocial API')

app.include_router(users_routes.router)


@app.get('/', status_code=HTTPStatus.OK, response_model=MessageSchema)
def read_root():
    return {'message': 'Olá Mundo!'}
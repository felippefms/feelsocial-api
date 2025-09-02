from http import HTTPStatus

from fastapi import APIRouter

from feelsocial_api.models import User
from ..schemas.user_schema import UserPublic, UserSchema, UserList

router = APIRouter(prefix='/users', tags=['users'])

# @router.get('/', response_model=UserList)
# def read_users(session: Session, skip: int = 0, limit: int = 100):
#     users = session.scalars(select(User).offset(skip).limit(limit)).all()
#     return {'users': users}


@router.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: UserSchema):
    return user

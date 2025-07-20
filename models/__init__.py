from sqlalchemy.orm import registry

from .user_model import User as User

table_registry = registry()

Base = table_registry.generate_base()

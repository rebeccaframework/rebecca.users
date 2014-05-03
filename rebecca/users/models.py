import hashlib
from sqlalchemy import (
    Column,
    Integer,
    MetaData,
    String,
    Table,
    Unicode,
)
# from sqlalchemy.orm import (
#     relationship,
# )

METADATA = MetaData()
USER_TABLE = Table(
    "users", METADATA,
    Column("id", Integer, primary_key=True),
    Column("username", Unicode(255), unique=True, nullable=False),
    Column("password_digest", String(255), nullable=False),
)


class User(object):
    """ user model """
    def __init__(self, username=None, password=None):
        self.password_digest = None
        self.username = username
        self.password = password

    def hash_password(self, password):
        if password is None:
            return None
        return hashlib.sha1(password.encode('utf-8')).hexdigest()

    def set_password(self, password):
        self.password_digest = self.hash_password(password)

    password = property(fset=set_password)

    def validate_password(self, password):
        return self.password_digest == self.hash_password(password)

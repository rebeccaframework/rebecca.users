from zope.interface import implementer
from .interfaces import IAuthenticator


@implementer(IAuthenticator)
class UserAuthenticator(object):
    def __init__(self, db_session, user_model):
        self.db_session = db_session
        self.user_model = user_model

    def query(self, username):
        query = self.db_session.query(
            self.user_model
        ).filter(
            self.user_model.username == username
        )
        return query

    def authenticate(self, username, password):
        user = self.query(username).first()
        if user is None:
            return None

        if not user.validate_password(password):
            return None

        return user

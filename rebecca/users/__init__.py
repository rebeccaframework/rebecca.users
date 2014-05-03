from .interfaces import IAuthenticator
from .authenticator import UserAuthenticator
from .models import User, init


def includeme(config):
    init()
    db_session = config.registry.settings.get('rebecca.users.db_session')
    db_session = config.maybe_dotted(db_session)
    user_model = config.registry.settings.get('rebecca.users.user_model',
                                              User)
    user_model = config.maybe_dotted(user_model)
    config.registry.registerUtility(UserAuthenticator(db_session, user_model),
                                    IAuthenticator)

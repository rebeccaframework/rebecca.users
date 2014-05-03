""" api to use this library
"""

from .interfaces import IAuthenticator
from .models import METADATA


def authenticate(request, username, password):
    """ authenticate credentials
    :return: User
    """
    reg = request.registry
    authenticator = reg.utilities.lookup([], IAuthenticator, "")
    return authenticator.authenticate(username, password)


def create_tables(engine):
    METADATA.create_all(bind=engine)


def drop_tables(engine):
    METADATA.drop_all(bind=engine)

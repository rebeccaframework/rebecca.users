""" api to use this library
"""

from .interfaces import IAuthenticator


def authenticate(request, username, password):
    """ authenticate credentials
    :return: User
    """
    reg = request.registry
    authenticator = reg.utilities.lookup([], IAuthenticator, "")
    return authenticator.authenticate(username, password)

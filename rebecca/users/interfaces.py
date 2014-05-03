from zope.interface import Interface


class IAuthenticator(Interface):

    def authenticate(username, password):
        """ authenticate credential """

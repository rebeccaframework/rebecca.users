import unittest.mock as mock
from pyramid import testing


class TestAuthenticate(object):

    def _call_fut(self, *args, **kwargs):
        from rebecca.users.api import authenticate
        return authenticate(*args, **kwargs)

    def test_it(self):
        from rebecca.users.interfaces import IAuthenticator
        authenticator = mock.Mock()
        user = object()
        authenticator.authenticate.return_value = user
        request = testing.DummyRequest()
        request.registry.registerUtility(authenticator, IAuthenticator)
        result = self._call_fut(request, "dummy-user", "secret")

        assert result == user

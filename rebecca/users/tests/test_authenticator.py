import unittest.mock as mock


class TestUserAuthenticator(object):

    def _get_target(self):
        from rebecca.users.authenticator import UserAuthenticator
        return UserAuthenticator

    def _make_one(self, *args, **kwargs):
        return self._get_target()(*args, **kwargs)

    def test_authenticate_no_user(self):
        user_model = mock.Mock()
        db_session = mock.Mock()
        mock_query = db_session.query.return_value
        mock_filter = mock_query.filter.return_value
        mock_filter.first.return_value = None
        target = self._make_one(db_session, user_model)
        result = target.authenticate('dummy_user', 'secret')

        assert result is None

    def test_authenticate_invalid(self):
        user_model = mock.Mock()
        db_session = mock.Mock()
        mock_query = db_session.query.return_value
        mock_filter = mock_query.filter.return_value
        mock_user = mock.Mock()
        mock_user.validate_password.return_value = False
        mock_filter.first.return_value = mock_user
        target = self._make_one(db_session, user_model)
        result = target.authenticate('dummy_user', 'secret')

        assert result is None
        mock_user.validate_password.assert_called_with('secret')

    def test_authenticate(self):
        user_model = mock.Mock()
        db_session = mock.Mock()
        mock_query = db_session.query.return_value
        mock_filter = mock_query.filter.return_value
        mock_user = mock.Mock()
        mock_user.validate_password.return_value = True
        mock_filter.first.return_value = mock_user
        target = self._make_one(db_session, user_model)
        result = target.authenticate('dummy_user', 'secret')

        assert result is mock_user
        mock_user.validate_password.assert_called_with('secret')

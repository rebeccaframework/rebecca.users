class TestUser(object):
    def _get_target(self):
        from rebecca.users.models import User
        return User

    def _make_one(self, *args, **kwargs):
        return self._get_target()(*args, **kwargs)

    def test_validate_password(self):
        target = self._make_one()
        target.password = 'secret'

        assert target.validate_password('secret')

from pyramid import testing


def setup_db():
    from sqlalchemy import create_engine
    from sqlalchemy.orm import (
        scoped_session,
        sessionmaker,
    )
    from zope.sqlalchemy import ZopeTransactionExtension
    engine = create_engine('sqlite:///')
    DBSession = scoped_session(
        sessionmaker(extension=ZopeTransactionExtension(),
                     bind=engine))
    from rebecca.users.api import create_tables, drop_tables
    drop_tables(engine)
    create_tables(engine)
    return DBSession


def teardown_db():
    import transaction
    transaction.abort()
    from sqlalchemy.orm import clear_mappers
    clear_mappers()


def login(request):
    from rebecca.users.api import authenticate
    username = request.POST['username']
    password = request.POST['password']
    if authenticate(request, username, password):
        return "OK"
    return "NG"


def make_user(db_session, username, password):
    from rebecca.users.models import User
    user = User(username, password)
    db_session.add(user)
    return user


class TestAuthentication(object):

    def test_not_authenticated(self):
        DBSession = setup_db()

        config = testing.setUp(
            settings={
                'rebecca.users.db_session': DBSession,
            })

        try:
            config.add_view(login, name='login')
            config.include('rebecca.users')
            request = testing.DummyRequest(registry=config.registry,
                                           POST={'username': 'dummy-user',
                                                 'password': 'secret'})
            result = login(request)
            assert result is "NG"

        finally:
            testing.tearDown()
            teardown_db()

    def test_authenticate(self):
        DBSession = setup_db()

        config = testing.setUp(
            settings={
                'rebecca.users.db_session': DBSession,
            })

        try:
            config.add_view(login, name='login')
            config.include('rebecca.users')
            make_user(DBSession, 'dummy-user', 'secret')
            request = testing.DummyRequest(registry=config.registry,
                                           POST={'username': 'dummy-user',
                                                 'password': 'secret'})
            result = login(request)
            assert result is "OK"

        finally:
            testing.tearDown()
            teardown_db()

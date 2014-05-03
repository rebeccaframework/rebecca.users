===================
rebecca.users
===================

.. image:: https://travis-ci.org/rebeccaframework/rebecca.users.svg?branch=master
   :target: https://travis-ci.org/rebeccaframework/rebecca.users


``rebecca.users`` is management user model and authentication.

Introduction
------------

:Github: https://github.com/rebeccaframework/rebecca.users


Installation
------------

::

  pip install rebecca.users

development::

  pip install git+ssh://git@github.com:rebeccaframework/rebecca.users.git


Quickstart
----------

::

   config.include('rebecca.users')

custom login view::

   def login(request):
       username = request.POST['username']
       password = request.POST['password']
       user = authenticate(request, username, password)
       if user:
           headers = security.remember(request, user.username)
           return HTTPFound(location='/', headers=headers)
       return dict()


User Guide
----------

*not* a reference, but a topical guide that covers the common situations and commands people need.


Reference Guide
---------------

settings
+++++++++++++++++


API
+++++++++++++++++++


Development
-----------

testing
+++++++++++

run tests for source tree::

  $ pip install -e .[testing]
  $ py.test

run all tests with tox::

  $ pip install tox
  $ tox


Release History
---------------

- the changelog
- don't use sections to mark releases, because it makes the TOC too noisy


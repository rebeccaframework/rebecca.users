from setuptools import setup, find_packages


requires = [
    "setuptools>=0.7",
    "pyramid",
    "sqlalchemy",
    "rebecca.repository",
]

tests_require = [
    "pytest",
    "pytest-cov",
    "zope.sqlalchemy",
]


setup(name="rebecca.users",
      namespace_packages=["rebecca"],
      packages=find_packages(),
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
          "testing": tests_require,
      },
)

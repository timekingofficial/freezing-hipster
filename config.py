import os
basedir = os.path.abspath(os.path.dirname(__file__))

CSRF_ENABLED = True
SECRET_KEY = '2435908a7wfuioaj349a7weofawuifhaeowf78a34'

OPENID_PROVIDERS = [
    { 'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id' }
]

# SQLALCHEMY_DATABASE_URI = "postgresql://admin:password@localhost/tkdb"
SQLALCHEMY_DATABASE_URI = "postgresql://localhost/tkdb"
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
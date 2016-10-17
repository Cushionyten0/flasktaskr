import os

# grab the folder where this script lives
basedir = os.path.abspath(os.path.dirname(__file__))

# configuration
DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = '\x16T3\x89}\xa94\xca,`Z\x97\xef\xff\xf0GO\xdbE\xc0\xc2\xb0\x8fr'

# define the full path for the database
DATABASE_PATH = os.path.join(basedir, DATABASE)

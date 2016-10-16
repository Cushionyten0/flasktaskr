import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = '\x1e\xe3B\xfc\xb6\xe7H\x17\xfc\xe2U\xe8a)-\xc7\x04\xa3\xce_T&tC'

DATABASE_PATH = os.path.join(basedir, DATABASE)

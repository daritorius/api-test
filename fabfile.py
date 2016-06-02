import os
from fabric.api import *

SITE_DIR = os.path.dirname(__file__)
VIRTUALENV_DIR = os.path.join(SITE_DIR, '.env/api')
VIRTUALENV_ACTIVATE = '. %s' % os.path.join(VIRTUALENV_DIR, 'bin', 'activate')


def init_virtualenv():
    local("virtualenv %s --no-site-packages --python=/usr/bin/python" % VIRTUALENV_DIR)
    with prefix(VIRTUALENV_ACTIVATE):
        local("pip install -r requirements.txt")
    local("touch database/api.db")
    local("sqlite3 database/api.db < database/schema.sql")

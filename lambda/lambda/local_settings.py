"""Settings for the local instance of our django app.  WARNING: this file should
not be committed or shared with others.
"""

import os
from urllib.parse import urlparse
# this is a test only setting file

# To set your local settings, edit the values below and change the name of this
# file to 'local_settings.py'

# A secret key can be generated by opening a django shell and running the
# get_secret_key() function. Copy and past it in below.
# python manage.py shell
# from django.core.management.utils import get_random_secret_key
# get_random_secret_key()
SECRET_KEY = "add a secret key here"

# Debug should be set to False for production environments, True for dev
# environments.
DEBUG = True

# This can be blank if debug is True else it should contain the names of the
# appropriate servers.
ALLOWED_HOSTS = []


# The bellow settings can be used to ensure that cookie data is only sent over
# secure HTTPS connections. Set them to True if this is the case. Note that this
# requires you to have HTTPS active on your site.
CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False

# Setting up you database. Bellow are settings for a MySQL batabase. If you
# leave these commented out your site will use a sqlite database.
# db_name = os.environ.get('db_username') + '$' + os.environ.get('db_name')
# db_lambda_username = os.environ.get('db_lambda_username')
# db_password = os.environ.get('db_password')
# db_hostname = os.environ.get('db_hostname')
# db_port = os.environ.get('db_port')

if os.environ.get('DATABASE_URL', '') != "":
    r = urlparse(os.environ.get('DATABASE_URL', ''))
    DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': os.path.relpath(r.path, "/"),
                'USER': r.username,
                'PORT': r.port,
                'PASSWORD': r.password,
                'HOST': r.hostname,
                # 'HOST': os.environ.get('db_hostname'), # this is for vpn
                'OPTIONS': {'ssl': 'require'},
            }
    }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': db_name,
#         'USER': db_lambda_username,
#         'PORT': db_port,
#         'PASSWORD': db_password,
#         'HOST': db_hostname,
#     }
# }

# Settings for a demo user that people can use without registering for their own
# account.  This user should be set up using an admin account and MUST have the
# profile.is_demo_user set to true.
DEMO_USER_USERNAME = "test"
DEMO_USER_PASSWORD = "test1"
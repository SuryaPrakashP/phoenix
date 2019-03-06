"""
WSGI config for myshop project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
<<<<<<< HEAD
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phoenix.settings")
application = get_wsgi_application()



# import hercules.wsgi
# SCRIPT_NAME = '/home/phoenix/hercules'

# class PassengerPathInfoFix(object):
#     """
#     Sets PATH_INFO from REQUEST_URI because Passenger doesn't provide it.
#     """
#     def __init__(self, app):
#         self.app = app

#     def __call__(self, environ, start_response):
#         from urllib.parse import unquote
#         environ['SCRIPT_NAME'] = SCRIPT_NAME

#         request_uri = unquote(environ['REQUEST_URI'])
#         script_name = unquote(environ.get('SCRIPT_NAME', ''))
#         offset = request_uri.startswith(script_name) and len(environ['SCRIPT_NAME']) or 0
#         environ['PATH_INFO'] = request_uri[offset:].split('?', 1)[0]
#         return self.app(environ, start_response)

# application = hercules.wsgi.application
# application = PassengerPathInfoFix(application)
=======

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phoenix.settings')

application = get_wsgi_application()
>>>>>>> 9d8f6fa8ea11d7eafe6fabed39b3e5c9bd32690e

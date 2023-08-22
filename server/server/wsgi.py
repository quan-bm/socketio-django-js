"""
WSGI config for server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os
import time

from django.core.wsgi import get_wsgi_application
import socketio

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

application = get_wsgi_application()

sio = socketio.Server(async_mode='eventlet', cors_allowed_origins='*')

application = socketio.WSGIApp(sio, application)


@sio.event
def connect(sid, environ, auth):
    print('connect ', sid)


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.on("hello")
def handle_hello(sid, data):
    print("message from client:", data)
    time.sleep(5)
    sio.emit("hello-response", "hello client", room=sid)

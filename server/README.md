# SocketIO implementation for Django server
---
# Packages
```text
Django==4.2.4 
django-cors-headers==4.2.0 
eventlet==0.33.3
python-socketio==5.8.0
```

# Run the server
```bash
gunicorn -k eventlet server.wsgi:application --reload
```
Reference: https://www.botreetechnologies.com/blog/django-websocket-with-socketio/

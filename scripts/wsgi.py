"""WSGI entrypoint for a production server (gunicorn/render).

`serve.py` builds the Flask `app` at import time, so gunicorn can load it
directly: `gunicorn --chdir scripts wsgi:app`.
"""
from serve import app  # noqa: F401

from functools import wraps
import json
import logging

from .auth import get_oauth_session
from .settings import get_settings

_log = logging.getLogger(__name__)


def with_default_headers(f):

    @wraps(f)
    def wrapper(*args, **kw):
        if 'headers' not in kw:
            kw['headers'] = {
                'content-type': 'application/json',
            }
        return f(*args, **kw)

    return wrapper


class Tinbox:
    def __init__(self):
        self.session = get_oauth_session()
        self.settings = get_settings()

    def get_url(self, *args, **kw):
        return self.settings.get_url(*args, **kw)

    def _get_default_headers(self):
        return {
            'content-type': 'application/json'
        }

    @with_default_headers
    def post(self, path, *args, **kw):
        return self.session.post(self.get_url(path), *args, **kw)

    @with_default_headers
    def put(self, path, *args, **kw):
        return self.session.put(self.get_url(path), *args, **kw)

    def get(self, path, *args, **kw):
        return self.session.get(self.get_url(path), *args, **kw)

    def create_ticket(self, sender_email, subject, body, sender_name=None,
                      context=None, attachments=None):
        data = {'sender_email': sender_email,
                'sender_name': sender_name,
                'subject': subject,
                'body': body,
                'attachments': attachments}

        if context is not None:
            data.update({'pks': context})

        request = self.post('tickets/',
                            data=json.dumps(data))

        return request.json()

    def upload_attachment(self, attachment_pk, attachment_bytes):
        return self.put(
            'attachments/{}/'.format(attachment_pk),
            data=attachment_bytes,
            headers={
                'content-type': 'application/binary'
            }
        ).json()

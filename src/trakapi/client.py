import logging

from .auth import get_oauth_session
from .settings import get_settings

_log = logging.getLogger(__name__)


class Trak:
    def __init__(self):
        self.session = get_oauth_session()
        self.settings = get_settings()

    def get_url(self, *args, **kw):
        return self.settings.get_url(*args, **kw)

    def post(self, path, *args, **kw):
        return self.session.post(self.get_url(path), *args, **kw)

    def create_ticket(self, sender_email, subject, body):
        request = self.post('tickets/',
                            data={'sender_email': sender_email,
                                  'subject': subject,
                                  'body': body})

        return request.json()


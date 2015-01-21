from functools import wraps
import logging
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError

from .auth import get_oauth_session, fetch_token
from .settings import get_settings

_log = logging.getLogger(__name__)


def renew_token(session=None):
    """
    Decorator to renew the token for the specified session if a
    TokenExpiredError is raised when running the decorated functions.

    If no session is provided, the decorator will look at the first argument
    of the decorated function for a *session* attribute.

    :param session: OAuth2Session
    """
    def renew_token_decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            nonlocal session

            if session is None:
                self, *_ = args

                try:
                    session = getattr(self, 'session')
                except AttributeError:
                    raise ValueError(
                        'session is not provided to the decorator, ond the '
                        '\'session\' attribute can\'t be found on the first '
                        'argument to the decorated function.')

            try:
                return func(*args, **kw)
            except TokenExpiredError:
                _log.info('Access token for %s expired, requesting a new '
                          'token.', session)
                fetch_token(session)
                return func(*args, **kw)

        return wrapper

    return renew_token_decorator


class Trak:
    def __init__(self):
        self.session = get_oauth_session()
        self.settings = get_settings()

    def get_url(self, *args, **kw):
        return self.settings.get_url(*args, **kw)

    @renew_token()
    def post(self, path, *args, **kw):
        return self.session.post(self.get_url(path), *args, **kw)

    @renew_token()
    def get(self, path, *args, **kw):
        return self.session.get(self.get_url(path), *args, **kw)

    def create_ticket(self, sender_email, subject, body):
        request = self.post('tickets/',
                            data={'sender_email': sender_email,
                                  'subject': subject,
                                  'body': body})

        return request.json()


from oauthlib.oauth2.rfc6749.clients.backend_application import \
    BackendApplicationClient
from requests_oauthlib.oauth2_session import OAuth2Session

from .settings import get_settings


def get_oauth_session():
    """
    Handles OAuth2 authentication.
    :return: A requests-oauthlib OAuth2Session.
    """
    settings = get_settings()

    # TODO: Refactor to allow any OAuth2 client type, maybe let
    # implementations handle OAuth2Session init themselves?

    session = OAuth2Session(
        client_id=settings.client_id,
        client=BackendApplicationClient(settings.client_id)
    )

    session.fetch_token(settings.get_url('oauth2/token/'),
                        client_id=settings.client_id,
                        client_secret=settings.client_secret,
                        scope=settings.scope)

    return session
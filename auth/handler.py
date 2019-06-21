import urllib
from uuid import uuid4

from common.lib import (log_event, make_log, make_response,)

log = make_log(__file__, log_level='debug')

AUTH_DOMAIN = 'https://5bgjniisic.auth.us-east-1.amazoncognito.com'
AUTH_ENDPOINT = f'{AUTH_DOMAIN}/login'
APP_CLIENT_ID = '4la5m8d01u3g5d0nduta59rndl'
REDIRECT_URI = 'https://5bgjniisic.execute-api.us-east-1.amazonaws.com/dev/secret'
OAUTH2_SCOPES = 'openid email'


def get(event, context):
    """Respond to an HTTP GET."""
    log_event(log, event)
    log.info('Hello, Auth!')
    params = {
        'client_id': APP_CLIENT_ID,
        'redirect_uri': REDIRECT_URI,
        'reponse_type': 'code',
        # 'state': str(uuid4()).replace('-', ''),
        'scope': OAUTH2_SCOPES,
    }
    encoded_params = urllib.parse.urlencode(params)
    auth_url = f'{AUTH_ENDPOINT}?{encoded_params}'
    return make_response(301, None, headers={'location': auth_url})

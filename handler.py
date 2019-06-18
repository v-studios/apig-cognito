from lib import (log_event, make_log, make_response,)

log = make_log(log_level='debug')


def get(event, context):
    """Respond to an HTTP GET."""
    log_event(log, event)
    log.info('Hello, world!')
    return make_response(200, {})

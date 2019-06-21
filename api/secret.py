from common.lib import (log_event, make_log, make_response,)

log = make_log(__file__, log_level='debug')


def get(event, context):
    """Respond to an HTTP GET."""
    log_event(log, event)
    return make_response(200, {'message': 'Hello, Agent!'})

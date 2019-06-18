import os
import json
import logging

DEFAULT_FORMAT_STR = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'


def log_event(log, event):
    log.debug(f'event={json.dumps(event)}')


def make_log(caller_fname, log_level='info', log_fmt_str=DEFAULT_FORMAT_STR):
    # Convert log_level arg to logging module value.
    level = getattr(logging, log_level.upper())
    # Name logger after calling script's name.
    logger_name = os.path.split(caller_fname)[-1].replace('.py', '')
    # Prepare a formatter for the log stream handler.
    formatter = logging.Formatter(log_fmt_str)
    # Make a logger w/ the right name.
    log = logging.getLogger(logger_name)
    # Set to DEBUG because no other handlers can go higher than the base level.
    log.setLevel(logging.DEBUG)
    # Create a console handler w/ the correct format & specified log level.
    ch = logging.StreamHandler()
    ch.setLevel(level)
    ch.setFormatter(formatter)
    # Silence boto.
    for lib in ('boto', 'boto3', 'botocore'):
        logging.getLogger(lib).setLevel(logging.WARNING)
    return log


def make_response(status_code, body):
    return {
        'statusCode': status_code,
        'body': json.dumps(body),
    }

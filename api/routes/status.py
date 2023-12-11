"""
API endpoints that carry information regarding server uptime, load, etc.
"""

import datetime

from flask import Blueprint

initTime = datetime.datetime.now()

status = Blueprint('status', __name__, url_prefix='/status')

@status.route('/uptime')
def get_uptime() -> dict[str, str]:
    """
    Get the number of hours, minutes, and seconds since program launch,
    as well as the actual time thereof.

    Endpoint: /status/uptime

    :return: the start date and the time elapsed since
    """
    return {
        'started': str(initTime),
        'elapsed': str(datetime.datetime.now() - initTime)
    }

@status.route('/is-up/<port>')
def is_port_in_use(port: str) -> dict[str, str]:
    """
    Get the current status of the passed port.

    Endpoint: /status/is-up/{port}

    :param int port: the port (and hence service) being queried
    :return: the boolean status
    """
    import socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return {
            'up-status': str(sock.connect_ex(('localhost', int(port))) == 0)
        }

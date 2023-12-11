"""
API endpoints that carry information regarding server uptime, load, etc.
"""

import datetime

from flask import Blueprint

initTime = datetime.datetime.now()

status = Blueprint('status', __name__, url_prefix='/status')

@status.route('/uptime')
def get_uptime():
    """
    Returns the number of hours, minutes, and seconds since program launch,
    as well as the actual time thereof.

    Endpoint: /status/uptime
    """
    return {
        'started': str(initTime),
        'elapsed': str(datetime.datetime.now() - initTime)
    }

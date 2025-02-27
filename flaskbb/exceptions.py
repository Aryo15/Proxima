"""
flaskbb.exceptions
~~~~~~~~~~~~~~~~~~

Exceptions implemented by Ekaayam.

:copyright: (c) 2015 by the EkaayamB Team.
:license: BSD, see LICENSE for more details
"""

from werkzeug.exceptions import Forbidden, HTTPException

from .core.exceptions import BaseEkaayamError


class EkaayamHTTPError(BaseEkaayamError, HTTPException):
    description = "An internal error has occured"


EkaayamError = EkaayamHTTPError


class AuthorizationRequired(EkaayamError, Forbidden):
    description = "Authorization is required to access this area."


class AuthenticationError(EkaayamError):
    description = "Invalid username and password combination."

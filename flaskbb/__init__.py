# -*- coding: utf-8 -*-
"""
flaskbb
~~~~~~~

Ekaayam is a forum software written in python using the
microframework Flask.

:copyright: (c) 2014 by the Ekaayam Team.
:license: BSD, see LICENSE for more details.
"""

__version__ = "2.1.0"

import logging

logger = logging.getLogger(__name__)

from flaskbb.app import create_app  # noqa

# -*- coding: utf-8 -*-
"""
flaskbb.utils.settings
~~~~~~~~~~~~~~~~~~~~~~

This module contains the interface for interacting with Ekaayam's
configuration.

:copyright: (c) 2014 by the Ekaayam Team.
:license: BSD, see LICENSE for more details.
"""

import logging
from collections.abc import MutableMapping

from flaskbb.management.models import Setting

logger = logging.getLogger(__name__)


class EkaayamConfig(MutableMapping):
    """Provides a dictionary like interface for interacting with Ekaayam's
    Settings cache.
    """

    def __init__(self, *args, **kwargs):
        self.update(dict(*args, **kwargs))

    def __getitem__(self, key):
        try:
            return Setting.as_dict()[key]
        except KeyError:
            logger.info(f"Couldn't find setting for key ${key}")
            return None

    def __setitem__(self, key, value):
        Setting.update({key.lower(): value})

    def __delitem__(self, key):  # pragma: no cover
        pass

    def __iter__(self):
        return iter(Setting.as_dict())

    def __len__(self):
        return len(Setting.as_dict())


flaskbb_config = EkaayamConfig()

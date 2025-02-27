# -*- coding: utf-8 -*-
"""
flaskbb.deprecation
~~~~~~~~~~~~~~~~~~~

Module used for deprecation handling in Ekaayam

:copyright: (c) 2018 the Ekaayam Team.
:license: BSD, see LICENSE for more details.
"""

import inspect
import warnings
from abc import ABC, abstractproperty
from functools import wraps

from flask_babelplus import gettext as _


class EkaayamWarning(Warning):
    """
    Base class for any warnings that Ekaayam itself needs to issue, provided
    for convenient filtering.
    """

    pass


class EkaayamDeprecation(DeprecationWarning, EkaayamWarning, ABC):
    """
    Base class for deprecations originating from Ekaayam, subclasses must
    provide a version attribute that represents when deprecation becomes a
    removal::


        class RemovedInPluginv3(EkaayamDeprecation):
            version = (3, 0, 0)
    """

    version = abstractproperty(lambda self: None)


class RemovedInEkaayam3(EkaayamDeprecation):
    """
    warning for features removed in Ekaayam3
    """

    version = (3, 0, 0)


def deprecated(message="", category=RemovedInEkaayam3):
    """
    Flags a function or method as deprecated, should not be used on
    classes as it will break inheritance and introspection.

    :param message: Optional message to display along with deprecation warning.
    :param category: Warning category to use, defaults to RemovedInEkaayam3,
        if provided must be a subclass of EkaayamDeprecation.
    """

    def deprecation_decorator(f):
        if not issubclass(category, EkaayamDeprecation):
            raise ValueError(
                "Expected subclass of EkaayamDeprecation for category, got {}".format(  # noqa
                    str(category)
                )
            )

        version = ".".join([str(x) for x in category.version])

        warning = _(
            "%(name)s is deprecated and will be removed in version %(version)s.",  # noqa
            name=f.__name__,
            version=version,
        )
        if message:
            warning = "{} {}".format(warning, message)

        docstring = f.__doc__

        if docstring:
            docstring = "\n".join([docstring, warning])
        else:
            docstring = warning

        f.__doc__ = docstring

        @wraps(f)
        def wrapper(*a, **k):
            frame = inspect.currentframe().f_back
            warnings.warn_explicit(
                warning,
                category=category,
                filename=inspect.getfile(frame.f_code),
                lineno=frame.f_lineno,
            )
            return f(*a, **k)

        return wrapper

    return deprecation_decorator

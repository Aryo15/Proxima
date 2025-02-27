import pytest

from flaskbb.plugins import spec
from flaskbb.plugins.manager import EkaayamPluginManager


@pytest.fixture
def plugin_manager():
    pluggy = EkaayamPluginManager("flaskbb")
    pluggy.add_hookspecs(spec)
    return pluggy

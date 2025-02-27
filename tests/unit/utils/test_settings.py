from flaskbb.utils.settings import EkaayamConfig


def test_flaskbb_config(default_settings):
    flaskbb_config = EkaayamConfig()

    assert len(flaskbb_config) > 0
    # test __getitem__
    assert flaskbb_config["PROJECT_TITLE"] == "Ekaayam"
    # test __setitem__
    flaskbb_config["PROJECT_TITLE"] = "EkaayamTest"
    assert flaskbb_config["PROJECT_TITLE"] == "EkaayamTest"
    # test __iter__
    assert "PROJECT_TITLE" in list(flaskbb_config.__iter__())

import pytest


@pytest.fixture
def dev_config():
    print("Loading Development Configuration")
    return {"db": "dev_db", "debug": True}


@pytest.fixture
def prod_config():
    print("Loading Production Configuration")
    return {"db": "prod_db", "debug": False}


def test_dev_config_loading(dev_config):
    # Directly use the dev_config fixture
    print(f"Testing with Development Config: {dev_config}")
    assert dev_config["debug"] is True
    assert dev_config["db"] == "dev_db"


@pytest.mark.parametrize("env_name", ["dev_config", "prod_config"])
def test_config_loading(env_name, request):
    # Dynamically get the correct fixture based on the env_name
    config = request.getfixturevalue(env_name)
    print(f"Testing with: {config}")

    # Perform different assertions based on the environment
    if env_name == "dev_config":
        assert config["debug"] is True
        assert config["db"] == "dev_db"
    else:
        assert config["debug"] is False
        assert config["db"] == "prod_db"

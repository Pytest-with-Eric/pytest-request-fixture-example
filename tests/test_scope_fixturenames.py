import pytest


@pytest.fixture(scope="module")
def setup_module():
    print("Setting up module")
    return "Module setup"


@pytest.fixture(scope="function")
def setup_function():
    print("Setting up function")
    return "Function setup"


def test_example(request, setup_module, setup_function):
    print(f"Test scope: {request.scope}")
    print(f"Active fixtures: {request.fixturenames}")
    assert "setup_function" in request.fixturenames
    assert "setup_module" in request.fixturenames

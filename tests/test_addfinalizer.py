import pytest


@pytest.fixture
def resource_setup(request):
    print("Resource setup")

    def resource_teardown():
        print("Resource teardown")

    request.addfinalizer(resource_teardown)
    return "Resource"


def test_resource(resource_setup):
    print("Testing with resource")
    assert resource_setup == "Resource"

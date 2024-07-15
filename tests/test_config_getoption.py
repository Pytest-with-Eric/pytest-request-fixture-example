import pytest


@pytest.fixture(scope="session")
def db_url(request):
    """Fixture to retrieve the database URL."""
    return request.config.getoption("--dburl")


def test_get_db_url(request):
    db_url = request.config.getoption("--dburl")
    print(f"db_url: {db_url}")
    assert db_url is not None


def test_get_db_url_fixture(db_url):
    print(f"db_url: {db_url}")
    assert db_url is not None

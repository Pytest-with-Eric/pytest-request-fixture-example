import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--dburl",  # For Postgres use "postgresql://user:password@localhost/dbname"
        action="store",
        default="sqlite:///./test_db.db",  # Default uses SQLite in memory db
        help="Database URL to use for tests.",
    )


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

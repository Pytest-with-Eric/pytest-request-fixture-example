def pytest_addoption(parser):
    parser.addoption(
        "--dburl",  # For Postgres use "postgresql://user:password@localhost/dbname"
        action="store",
        default="sqlite:///./test_db.db",  # Default uses SQLite in memory db
        help="Database URL to use for tests.",
    )

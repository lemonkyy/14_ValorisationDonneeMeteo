from .settings import *

# Use SQLite for tests to avoid requiring TimescaleDB.
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test.sqlite3",
    }
}

# Skip weather app migrations during tests, because they contain TimescaleDB-specific SQL.
MIGRATION_MODULES = {
    "weather": None,
}

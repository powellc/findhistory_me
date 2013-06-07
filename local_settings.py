
DEBUG = True
AWS_ACCESS_KEY_ID = 'AKIAIC6KSWVHASDPKERQ'
AWS_SECRET_ACCESS_KEY = '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'

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

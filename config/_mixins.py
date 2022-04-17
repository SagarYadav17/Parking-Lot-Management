from os import environ


SECRET_KEY = environ.get("DJANGO_SECRET_KEY")

# Database
DB_NAME = environ.get("DB_NAME", "parking")
DB_USER = environ.get("DB_USER", "postgres")
DB_PASSWORD = environ.get("DB_PASSWORD", "postgres")
DB_HOST = environ.get("DB_HOST", "localhost")
DB_PORT = environ.get("DB_PORT", "5432")

# Redis
REDIS_URL = environ.get("REDIS_URL", "redis://localhost:6379")

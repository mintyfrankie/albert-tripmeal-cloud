from typing import Dict, Tuple, Any
import pymysql
from urllib import parse as urlparse
import os
from pymysql.connections import Connection
from pymysql.cursors import Cursor

__all__ = ["connection"]

# Initialize urlparse for mysql
urlparse.uses_netloc.append("mysql")

# Initialize DATABASES dict
DATABASES: Dict[str, Dict[str, Any]] = {
    "default": {
        "NAME": os.environ["DATABASE_NAME"],
        "USER": os.environ["DATABASE_USER"],
        "PASSWORD": os.environ["MYSQL_ROOT_PASSWORD"],
        "HOST": os.environ["DATABASE_HOST"],
        "PORT": os.environ["DATABASE_PORT"],
        "ENGINE": "django.db.backends.mysql",
    }
}


def connection() -> Tuple[Cursor, Connection]:
    """Create database connection and return cursor and connection objects.

    Returns:
        Tuple containing database cursor and connection objects
    """
    conn = pymysql.connect(
        host=DATABASES["default"]["HOST"],
        user=DATABASES["default"]["USER"],
        password=DATABASES["default"]["PASSWORD"],
        database=DATABASES["default"]["NAME"],
    )
    c = conn.cursor()
    return c, conn
